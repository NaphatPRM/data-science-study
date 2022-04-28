import pandas as pd
import numpy as np
import argparse, os, random
from util import timestr_to_seconds, drop_incomplete_rows, RANDOM_SEED
from stats_tests import one_sample_ttest, two_sample_ttest, paired_ttest, \
    chisquared_independence_test


##### STENCIL #####

def parse_args():
    parser = argparse.ArgumentParser(description="stats test runner")
    parser.add_argument('-d', help="path to data", default="./../data/college-data.csv")
    parser.add_argument('-s', help="scenario: ['one', 'two', 'three', 'four', 'five', 'all']")
    return parser.parse_args()


############ STUDENT WORK ############

# Columns:  Index(['ids', 'bday', 'enrolldate', 'expgradate', 'Rank', 'Major', 'Gender',
#        'Athlete', 'Height', 'Weight', 'Smoking', 'Sprint', 'MileMinDur',
#        'English', 'Reading', 'Math', 'Writing', 'State', 'LiveOnCampus',
#        'HowCommute', 'CommuteTime', 'SleepTime', 'StudyTime'],
#       dtype='object')


def scenario_one(dataset):
    """
    Scenario:
        - In our sample data, students reported their typical time 
        to run a mile, and whether or not they were an athlete. We want to know
        whether the average time to run a mile is different for athletes versus
        non-athletes.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    newdataset = drop_incomplete_rows(dataset[["Athlete", "MileMinDur"]])
    newdataset['MileMinDur'] = newdataset['MileMinDur'].apply(lambda row: timestr_to_seconds(row))
    athlete_rows = newdataset[newdataset["Athlete"] == 1]
    non_athlete_rows = newdataset[newdataset["Athlete"] == 0]

    test_statistic, p_value = two_sample_ttest(athlete_rows["MileMinDur"].to_numpy(),
                                               non_athlete_rows["MileMinDur"].to_numpy())

    tstats, pvalue = test_statistic, p_value

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_two(dataset):
    """
    Scenario:
        - The mean height of U.S. adults ages 20 and older is about 66.5
        inches (69.3 inches for males, 63.8 inches for females). In our
        sample data, we have a sample of 435 college students from a 
        single college.  We want to determine whether the mean height of 
        students at this college is significantly different than the mean 
        height of U.S. adults ages 20 and older.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    newdataset = drop_incomplete_rows(dataset[["Height"]])
    newdataset["Height"] = newdataset["Height"].apply(lambda row: float(row))
    heightarray = newdataset["Height"].to_numpy()
    test_statistic, p_value = one_sample_ttest(heightarray, 66.5)
    tstats, pvalue = test_statistic, p_value

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_three(dataset):
    """
    Scenario:
        - In the sample data, the students also reported their class rank,
        as well as whether they live on campus. We want to test if there 
        is a relationship between one's class rank and whether they live
        on campus.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    newdataset = drop_incomplete_rows(dataset[["Rank", "LiveOnCampus"]])
    test_statistic, p_value = chisquared_independence_test(newdataset, "Rank", "LiveOnCampus")
    tstats, pvalue = test_statistic, p_value

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_four(dataset):
    """
    Scenario:
        - The students in the sample completed all 4 placement tests for
        four subject areas - English, Reading, Math, and Writing - when they
        enrolled in the university. The scores are out of 100 points, and are
        present in the dataset. We want to test if there was a significant 
        difference between the average of the English test scores and that of 
        the Math test scores.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    newdataset = drop_incomplete_rows(dataset[["English", "Math"]])
    newdataset["English"] = newdataset["English"].apply(lambda row: float(row))
    newdataset["Math"] = newdataset["Math"].apply(lambda row: float(row))
    test_statistic, p_value = paired_ttest(newdataset["English"].to_numpy(), newdataset["Math"].to_numpy())
    tstats, pvalue = test_statistic, p_value

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_five(dataset):
    """
    Scenario:
        - In the sample dataset, respondents were asked their gender and whether
        or not they were a cigarette smoker. There were three answer choices: Nonsmoker, 
        Past smoker, and Current smoker. We want to test the relationship between 
        smoking behavior (nonsmoker, current smoker, or past smoker) and gender 
        (male or female).
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    newdataset = drop_incomplete_rows(dataset[["Smoking", "Gender"]])
    test_statistic, p_value = chisquared_independence_test(newdataset, "Smoking", "Gender")
    tstats, pvalue = test_statistic, p_value

    # TODO: Return tstats and pvalue
    return tstats, pvalue


########## DO NOT CHANGE THIS PART OF THE CODE ##########

if __name__ == "__main__":
    random.seed()
    args = parse_args()
    data_path, scenario_type = args.d, args.s
    stype_to_fname = {
        "one": scenario_one,
        "two": scenario_two,
        "three": scenario_three,
        "four": scenario_four,
        "five": scenario_five
    }

    # check the args input
    assert os.path.exists(args.d)
    assert scenario_type in stype_to_fname or scenario_type == "all"

    # Reading the dataset (college-data.csv)
    df = pd.read_csv(args.d)

    # and then call all the function
    if scenario_type == "all":
        for num in ["one", "two", "three", "four", "five"]:
            f = stype_to_fname[num]
            print(f"Running test for scenario {num}")
            stype_to_fname[num](df)
            print("------------------------------")
    # if not, then just one function itself
    else:
        print(f"Running test for scenario {scenario_type}")
        stype_to_fname[scenario_type](df)
