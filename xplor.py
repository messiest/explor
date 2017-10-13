import numpy as np
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt


class EDA:

    def __init__(self, data=None):
        self.data = data

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def analyze(self, plot=False):

        # assert self.data, "You must load data to run the analysis"

        if type(self.data) == pd.DataFrame:
            self.analyze_df(self.data, plot)
        elif type(self.data) == pd.Series:
            self.analyze_series(self.data, plot)
        else:
            "Type {} is currently unsupported.\n\nPlease post support requests on GitHub.\nBest,\n- @messiest"


    def analyze_series(self, df, plot=False):  # TODO @messiest change parameter name
        """

        :param df: Data to run data analysis on
        :type df: pandas DataFrame
        :return: None
        :rtype: None
        """
        assert type(df) is pd.Series, "Expected pandas.Series, {} is type {}".format(df, type(df))

        print("Series Name:\n-  {}".format(df.name))
        print("Data Type: {}\n".format(df.dtype))
        print("Unique Values: {}\n".format(df.nunique()))
        print("Missing Values: {}".format(df.isnull().sum()))
        print("\n{}".format(df.describe(include='all')))

        if df.nunique() == 1:  # skip plotting for columns with only one value
            print("\n{} is homogeneous".format(df.name))
            return

        if df.nunique() == df.count():  # skip plotting when all values are unique
            print("\nIndex eligible - All values of {} are unique\n".format(df.name))

        # plotting
        if not plot:
            return
        else:
            if df.dtype in [np.int64, np.float64]:
                sns.distplot(df)
                plt.title(df.name)
            elif df.dtype in [np.object, datetime.datetime]:
                sns.countplot(df)
                plt.title(df.name)
            plt.show()

    def analyze_df(self, df, plot=False):
        """

        :param df: Data to run data analysis on
        :type df: pandas DataFrame
        :return: None
        :rtype: None
        """
        assert type(df) is pd.DataFrame, "Expected pandas.DataFrame, {} is type {}".format(df, type(df))

        print("Dataframe Index:\n-  {}".format(df.index))
        print("Dataframe Shape:\n-  {}".format(df.shape))
        for item in df:
            print("---" * 39)
            print("Feature: {}".format(item))
            print("Data Type: {}\n".format(df[item].dtypes))
            print("Unique Values: {}\n".format(df[item].nunique()))
            print("Missing Values: {}".format(df[item].isnull().sum()))
            print("\n{}".format(df[item].describe(include='all')))

            if df[item].nunique() == 1:  # skip plotting for columns with only one value
                print("\n{} is homogeneous".format(item))
                continue

            if df[item].nunique() == df[item].count():  # skip plotting when all values are unique
                print("\nIndex eligible - All values of {} are unique\n".format(item))
                continue

            # plotting
            if not plot:
                continue
            else:
                if df[item].dtype in [np.int64, np.float64]:
                    sns.distplot(df[item])
                    plt.title(item)
                elif df[item].dtype in [np.object, datetime.datetime]:
                    sns.countplot(df[item])
                    plt.title(item)
                plt.show()
