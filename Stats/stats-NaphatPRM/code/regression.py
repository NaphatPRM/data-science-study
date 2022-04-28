import numpy as np
import pandas as pd
import random
import statsmodels.api as sm
from statsmodels.tools import eval_measures
from sklearn.metrics import r2_score
from util import all_variable_names_in_df, train_test_split, RANDOM_SEED


def regression(train_df, test_df, ind_var_names: list, dep_var_name: str):
    """
    Implement Linear Regression using StatsModel.

    inputs:
        - train_df: a Pandas DataFrame, containing all the training samples
        - test_df: a Pandas DataFrame, containing all the testing samples
        - ind_var_names: a list of strings of independent variable columns
                        that we want to include in the model
        - dep_var_name: the name of the dependent variable of our model
    

    output:
        - mse_train: the mean-squared error of the model (trained on the training
                    data), evaluated on the training dataset
        - mse_test: the mean-squared error of the model (trained on the training
                    data), evaluated on the testing dataset
        - rsquared_val: the r-squared value of the model (trained on the training
                    data), evaluated on the testing dataset
    """
    # Stencil: Error check whether the input that you provided to the function is correct or not
    # Do not modify
    for df in [train_df, test_df]:
        assert all_variable_names_in_df(ind_var_names + [dep_var_name], df)

    # TODO: Convert from train_df and test_df, construct X_train, X_test, y_train, y_test, where
    # X_train is a numpy array of all the independent variable instances from train_df,
    # y_train is a numpy array of all the dependent variable instances from train_df,
    # and the same applies to X_test and y_test from test_df.
    # Hint: Look up (1) how to select a Pandas DataFrame B with a subset of columns from a given DataFrame A,
    #           and (2) how to use Pandas .to_numpy() function.
    X_train = train_df[ind_var_names].to_numpy()
    Y_train = train_df[dep_var_name].to_numpy()
    X_test = test_df[ind_var_names].to_numpy()
    Y_test = test_df[dep_var_name].to_numpy()
    # TODO: Using statsmodel, fit a linear regression model to the training dataset
    X_train = sm.add_constant(X_train)
    X_test = sm.add_constant(X_test)
    mod = sm.OLS(Y_train, X_train)
    res = mod.fit()
    # TODO: Using statsmodel's eval_measures, calculate the Mean-squared Error of the model above
    # (on the training dataset)
    mse_train_val = eval_measures.mse(res.predict(X_train), Y_train)

    # TODO: Similarly, calculate the Mean-squared Error of the model above (on the testing dataset)
    mse_test_val = eval_measures.mse(res.predict(X_test), Y_test)
    # TODO: Calculate the *test* R-squared value (using sklearn's r2_score function)
    rsq_value = r2_score(Y_test, res.predict(X_test))

    # TODO: Print out the summary to see more information as needed
    print(res.summary())
    # TODO: Return these values with whatever you found!
    mse_train, mse_test, rsquared_val = mse_train_val, mse_test_val, rsq_value

    # And return them! :)
    return mse_train, mse_test, rsquared_val


def main():
    # TODO: Load the data from the bike-sharing.csv file into a Pandas DataFrame. Do not change
    # the variable name /data/
    # Hint: Look at the Pandas' read_csv function
    data = pd.read_csv("data/bike-sharing.csv")

    # TODO: Print out the column names of data to know what features there are in the dataset
    print("Columns: ", data.columns)

    # TODO: Modify the list IND_VAR_NAMES to select the independent variables you want to perform
    # a linear regression on
    IND_VAR_NAMES = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum',
                     'windspeed']

    # Select the dependent variable name DEP_VAR_NAME (default is "cnt")
    DEP_VAR_NAME = "cnt"

    # TODO: Using the imported train_test_split function (from util.py), create the train_df and
    # test_df that will be passed into regression.
    train_df, test_df = train_test_split(data)

    # TODO: Call regression and perform other calculations as you deem necessary to answer the
    # questions posed for this section.
    mse_train, mse_test, rsquared_val = regression(train_df, test_df, IND_VAR_NAMES, DEP_VAR_NAME)
    print(mse_train)
    print(mse_test)
    print(rsquared_val)


############ DON'T MODIFY BELOW THIS LINE ############

if __name__ == "__main__":
    np.random.seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)
    main()
