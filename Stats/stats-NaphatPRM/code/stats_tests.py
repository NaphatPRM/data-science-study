import numpy as np
import pandas as pd
from util import all_variable_names_in_df
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency


def one_sample_ttest(values, population_mean):
    # TODO: Use scipy's ttest_1samp
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html)
    # to get the t-statistic and the p-value.
    tstats, pvalue = ttest_1samp(values, population_mean, axis=0, nan_policy='propagate')

    # TODO: Print out the tstats and pvalue to determine your answer
    # to the questions
    print("Value of T-stats" + str(tstats))
    print("Value of P-value" + str(pvalue))
    # and then we'll return tstats and pvalue
    return tstats, pvalue


def two_sample_ttest(values_a, values_b):
    ## Stencil: Error check input - do not modify this part

    # TODO: Use scipy's ttest_ind
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
    # to get the t-statistic and the p-value
    # Note: Be sure to make the function call in a way such that the code will disregard
    # null (nan) values. Additionally, you can assume equal variance.
    tstats, pvalue = ttest_ind(values_a, values_b)

    # TODO: You can print out the tstats, pvalue, and other necessary
    # calculations to determine your answer to the questions
    print("Value of T-stats" + str(tstats))
    print("Value of P-value" + str(pvalue))

    # and then we'll return tstats and pvalue
    return tstats, pvalue


def paired_ttest(values_a, values_b):
    # TODO: Use scipy's ttest_rel
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)
    # to get the test statistic and the p-value
    # Note: Be sure to make the function call in a way such that the code will disregard
    # null (nan) values.
    tstats, pvalue = ttest_rel(values_a, values_b, axis=0, nan_policy='propagate')

    # TODO: You can print out the tstats and pvalue to determine your answer
    # to the questions
    print("Value of T-stats" + str(tstats))
    print("Value of P-value" + str(pvalue))

    # and then we'll return tstats and pvalue
    return tstats, pvalue


def chisquared_independence_test(df, column_a_name, column_b_name):
    ## Stencil: Error check input - do not modify this part
    assert all_variable_names_in_df([column_a_name, column_b_name], df)

    # TODO: Create a cross table between the two columns a and b
    # Hint: If you are unsure how to do this, refer to the stats lab!
    cross_table = pd.crosstab(df[column_a_name], df[column_b_name])
    # TODO: Use scipy's chi2_contingency
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
    # to get the test statistic and the p-value
    tstats, pvalue, dof, expected = chi2_contingency(cross_table)

    # TODO: You can print out the test statistics and pvalue to determine your answer
    # to the questions

    print("Value of T-stats" + str(tstats))
    print("Value of P-value" + str(pvalue))
    # and then we'll return tstats and pvalue
    return tstats, pvalue
