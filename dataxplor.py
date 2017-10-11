import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt

def eda(dataframe):
    """
    Straight ganked from @ritikabhasker - https://github.com/ritikabhasker/Intro-to-EDA
    
    - 10/8/2017
        - Updated to python3
    - 10/10/2017
        - Reformatted output, updated the describe to include unique values @DaleWahl
        - Dropped, but @DaleWahl is still cool
    - 10/11/2017
        - Added feature plotting, and switched up the output format
        - Added assert, type coercion coming soon
    
    """
    assert type(dataframe) is pd.DataFrame, "Expected pandas.DataFrame, {} is type {}".format(dataframe, type(dataframe))
    
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
        

