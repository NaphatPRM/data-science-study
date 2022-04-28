#!/usr/bin/env python

import argparse
import json
import os
from os.path import dirname, realpath

from pyspark import SparkContext


def parse_args():
    parser = argparse.ArgumentParser(description='MapReduce join (Problem 2)')
    parser.add_argument('-d', help='path to data file', default='./../data/records.json')
    parser.add_argument('-n', help='number of data slices', default=128)
    parser.add_argument('-o', help='path to output JSON', default='output')
    return parser.parse_args()


# Feel free to create more mappers and reducers.
def mapper(record):
    # TODO
    return (record[2], [[record[0], record]])

def reducer1(a, b):
    return a + b

def mapper2(record):
    disp = []
    rele = []
    for element in record[1]:
        if element[0] == "disp":
            disp.append(element[1])
        elif element[0] == "rele":
            rele.append(element[1])
    if len(disp) != 0 and len(rele) != 0:
        return [(v, w) for v in rele for w in disp]
    else:
        return []

def mapper3(record):
    return record[0] + record[1]



def main():
    args = parse_args()
    sc = SparkContext()

    with open(args.d, 'r') as infile:
        data = [json.loads(line) for line in infile]
    
    # TODO: build your pipeline
    join_result = sc.parallelize(data, 128).map(mapper) \
        .reduceByKey(reducer1) \
        .flatMap(mapper2) \
        .sortByKey(True) \
        .map(mapper3) \
        .collect()
        
    print(join_result)
    sc.stop()

    if not os.path.exists(args.o):
        os.makedirs(args.o)

    with open(args.o + '/output_join.json', 'w') as outfile:
        json.dump(join_result, outfile, indent=4)


if __name__ == '__main__':
    main()
