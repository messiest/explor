import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt

def eda(dataframe):
    """

    :param dataframe: Data to run data analysis on
    :type dataframe: pandas DataFrame
    :return: None
    :rtype: None
    """
    assert type(dataframe) in [pd.DataFrame, pd.Series], "Expected pandas.DataFrame, {} is type {}".format(dataframe, type(dataframe))
    
    print("Dataframe Index:\n{}\n".format(dataframe.index))
    print("Dataframe Shape:\n{}\n".format(dataframe.shape))   
    for item in dataframe:
        print("---" * 39)
        print("Feature: {}".format(item))
        print("Data Type: {}\n".format(dataframe[item].dtypes))
        print("Unique Values: {}\n".format(dataframe[item].nunique()))
        print("Missing Values: {}".format(dataframe[item].isnull().sum()))
        print("\n{}".format(dataframe[item].describe(include='all')))
        
        # plotting
        if dataframe[item].nunique() == 1:  # skip plotting for columns with only one value
            print("\n{} is homogeneous".format(item))
            continue
            
        if dataframe[item].nunique() == dataframe[item].count():  # skip plotting when all values are unique
            print("\nIndex eligible - All values of {} are unique\n".format(item))
            continue
        
        if dataframe[item].dtype in [np.int64, np.float64]:
            sns.distplot(dataframe[item])
        elif dataframe[item].dtype in [np.object, dt.datetime]:
            sns.countplot(dataframe[item])
        plt.show()
        

