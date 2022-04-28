#!/usr/bin/env python

from __future__ import division
import argparse
import json
import math
from os.path import dirname, realpath
from pyspark import SparkContext
import time
import os

VIRTUAL_COUNT = 10
PRIOR_CORRELATION = 0.0
THRESHOLD = 0.5


##### Metric Functions ############################################################################
def correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy):
    # http://en.wikipedia.org/wiki/Correlation_and_dependence
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt(n * sum_xx - sum_x * sum_x) * math.sqrt(n * sum_yy - sum_y * sum_y)
    if denominator == 0:
        return 0.0
    return numerator / denominator


def regularized_correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy, virtual_count, prior_correlation):
    unregularized_correlation_value = correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy)
    weight = n / (n + virtual_count)
    return weight * unregularized_correlation_value + (1 - weight) * prior_correlation


def cosine_similarity(sum_xx, sum_yy, sum_xy):
    # http://en.wikipedia.org/wiki/Cosine_similarity
    numerator = sum_xy
    denominator = (math.sqrt(sum_xx) * math.sqrt(sum_yy))
    if denominator == 0:
        return 0.0
    return numerator / denominator


def jaccard_similarity(n_common, n1, n2):
    # http://en.wikipedia.org/wiki/Jaccard_index
    numerator = n_common
    denominator = n1 + n2 - n_common
    if denominator == 0:
        return 0.0
    return numerator / denominator


#####################################################################################################

##### util ##########################################################################################
def combinations(iterable, r):
    # http://docs.python.org/2/library/itertools.html#itertools.combinations
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(list(range(r))):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


#####################################################################################################


def parse_args():
    parser = argparse.ArgumentParser(description='MapReduce similarities')
    parser.add_argument('-d', help='path to data directory', default='./../data/recommendations/small/')
    parser.add_argument('-n', help='number of data slices', default=128)
    parser.add_argument('-o', help='path to output JSON', default="output")
    return parser.parse_args()


# Feel free to create more mappers and reducers.
def mapper0(record):
    # TODO
    list_record = record.split("::")
    if len(list_record) == 2:
        return (list_record[0], [list_record[1]])
    else:
        return (list_record[1], [[list_record[0], int(list_record[2])]])


def reducer(a, b):
    # TODO
    return a + b


def mapper1(record):
    # Hint: 
    # INPUT:
    #   record: (key, values)
    #     where -
    #       key: movie_id
    #       values: a list of values in the line
    # OUTPUT:
    #   [(key, value), (key, value), ...]
    #     where -
    #       key: movie_title
    #       value: [(user_id, rating)]
    # ./check_outputs_equal output/netflix_stage1_output.json ta_output/netflix_stage1_output.json
    # TODO
    name_movies = record[1][0]
    return (name_movies, record[1][1:])



def mapper2(record):
    title, review = record
    review_num = len(review)
    for a_review in review:
        user_id = a_review[0]
        rating = a_review[1]
        yield (user_id, [(title, rating, user_id, review_num)])

def calculateEverything(m, record):
    # Input : [movies_name, [(user, ratings), ...]]
    n = len(record)
    n1 = record[0][2]
    n2 = record[0][3]
    sum_x = sum(list(map(lambda x: x[0], record)))
    sum_y = sum(list(map(lambda x: x[1], record)))
    sum_xx = sum(list(map(lambda x: x[0] ** 2, record)))
    sum_yy = sum(list(map(lambda x: x[1] ** 2, record)))
    sum_xy = sum(list(map(lambda x: x[0] * x[1], record)))
    corr = correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy)
    reg_corr = regularized_correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy, VIRTUAL_COUNT, PRIOR_CORRELATION)
    cos_sim = cosine_similarity(sum_xx, sum_yy, sum_xy)
    jac_sim = jaccard_similarity(n, n1, n2)
    return [m, corr,reg_corr,cos_sim,jac_sim,n,n1,n2]

def mapper3(record):
    return (record[0], combinations(sorted(record[1]), 2))

def mapper4(record):
    # TODO
    return list(map(lambda x: ((x[0][0], x[1][0]), [(x[0][1], x[1][1],x[0][3], x[1][3])]), record[1]))

def mapper5(record):
    # TODO
    return (record[0][0], [calculateEverything(record[0][1], record[1])])

def mapper6(record):
    # TODO
    return list(map(lambda x: ((record[0], x[0]), x[1:]), record[1]))

def main():
    args = parse_args()
    sc = SparkContext()

    with open(args.d + '/movies.dat', 'r') as mlines:
        data = [line.rstrip() for line in mlines]
    with open(args.d + '/ratings.dat', 'r') as rlines:
        data += [line.rstrip() for line in rlines]

    # FEEL FREE TO EDIT ANY OF THE MAPPER/REDUCER FUNCTION CALLS, BUT ENSURE 
    # THE STAGE 1, STAGE 2, and FINAL RESULTS MATCH THE EXPECTED STRUCTURE

    # Implement your mapper and reducer function according to the following query.
    # stage1_result represents the data after it has been processed at the second
    # step of map reduce, which is after mapper1.
    stage1_result = sc.parallelize(data, args.n).map(mapper0).reduceByKey(reducer) \
        .map(mapper1).sortByKey(True)
    # print(stage1_result.collect())
    if not os.path.exists(args.o):
        os.makedirs(args.o)

    # Store the stage1_output
    with open(args.o + '/netflix_stage1_output.json', 'w') as outfile:
        json.dump(stage1_result.collect(), outfile, separators=(',', ':'))

    # TODO: continue to build the pipeline
    # Pay attention to the required format of stage2_result
    stage2_result = stage1_result.flatMap(mapper2).reduceByKey(reducer) \
        .map(mapper3).flatMap(mapper4).reduceByKey(reducer) \
        .map(mapper5).filter(lambda x: x[1][0][2] > 0.5).reduceByKey(reducer) \
        .sortByKey(True)

    # Store the stage2_outp
    with open(args.o + '/netflix_stage2_output.json', 'w') as outfile:
        json.dump(stage2_result.collect(), outfile, separators=(',', ':'))

    # TODO: continue to build the pipeline
    final_result = stage2_result.flatMap(mapper6).reduceByKey(reducer).collect()
    
    with open(args.o + '/netflix_final_output.json', 'w') as outfile:
        json.dump(final_result, outfile, separators=(',', ':'))

    sc.stop()


if __name__ == '__main__':
    main()
