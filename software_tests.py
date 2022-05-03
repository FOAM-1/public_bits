# -*- coding: utf-8 -*-
"""

    

"""

import koala.format_tools.format_tools as ft
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import BDay
import numpy as np


#------------------------------------------------------------------------------
#                               START OF FUNCTION
#------------------------------------------------------------------------------
def check_df_sum(df: pd.DataFrame, target: float = 1, absolute: bool = True, 
                 axis: int = 1) -> bool:
    
    
    """
    Description:
        
        Test used to check if dataframe sums to specific value along rows or
        columns. Sum can also be in absolute terms. Returns True if all elements
        sum to target, else fails assertion test.
        
    --------------------
    Inputs:
        
        df: pd.DataFrame -> data frame you want to test
        
        target: float -> the value you want your elements to sum to
        
        absolute: bool -> boolean value that lets you decide if you want the sum of
        the absolute values to equal the target or not
        
        axis: int -> the axis of the data frame you want to sum through
    
    --------------------
    Outputs:
        
        True, if all elements pass test. Else raises an assertion error

    
    """
    
    # checks that the df is actually a data frame
    assert (isinstance(df, pd.DataFrame)), "df variable must be pandas dataframe"
    
    # checks to see if you want df values to be absolute 
    if absolute:
        
        df = abs(df.copy())
        
    # sums along the desired axis, and then reduces the resulting series down to a list
    df_sum = df.sum(axis=axis).tolist()
    
    
    # loops through the list to check that each element (sum) is equal to the target
    for element in df_sum:
        
        assert (round(element, 4) == 1), f"failed sum test, value should be {target} but sum equals {round(element, 4)}"
    
    
    #  return True if all values pass test
    return True
#------------------------------------------------------------------------------
#                               END OF FUNCTION
#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
#                               START OF FUNCTION
#------------------------------------------------------------------------------
def check_date(idx: list, date = None, string: bool = False) -> bool:
    
    
    """
    Description:
        
        Checks to see if there is a specific date in an index. Used primarily
        to check if the last valid business day exists in an index. Setting date
        equal to None will check this.
        
    --------------------
    Inputs:
        
        idx: list -> index of a series of dataframe as a list
        
        date: can be either a string or datetime object
        
        string: bool -> converts whatever date you are looking to into a string
        format and searches for the string version in the idx variable
    
    --------------------
    Outputs:
        
        True, if the date exists in idx, else an assertion error is raised

    
    """
    
    # if no var is passed, then we just use the last business day
    if date is None:
    
        date = (datetime.now() - BDay(1)).date()
    
    # option to convert whatever date you use into a string
    if string: date = str(date)
    
    # check to see if the date is in the idx var
    assert (date in idx), f"{date} is not in the index"
    
    # if the test is passed then return True
    return True
#------------------------------------------------------------------------------
#                               END OF FUNCTION
#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
#                               START OF FUNCTION
#------------------------------------------------------------------------------
def df_value_comparison(a: pd.DataFrame, b: pd.DataFrame) -> bool:
    
    
    """
    Description:
        
        Checks to make sure that 
        
        i) the two dataframe have identical indexes and columns 
        ii) if nan values exist, that they exist in corresponding values
        e.g. if A.loc[x, y] == np.nan, then B.loc[x, y] also equals np.nan
        the implication here being that f(A) = B
        
        We can use this to check to ensure that if we have a valid price on a
        certain day, that we also have a signal on that same day. 
        
    --------------------
    Inputs:
        
        a: pd.DataFrame -> first dataframe
        
        b: pd.DataFrame -> second dataframe
    
    
    --------------------
    Outputs:
        
        True, if all checks are passed

    
    """
    
    # for this to work, the signals and prices dataframes must be the same size
    # and you must also have the same columns
    assert (set(a.columns) == set(b.columns)) & (set(a.index) == set(b.index)), "Columns and indexes are different"
    
    # loop through all the columns
    for column in a.columns.tolist():
        
        # loop through all the rows
        for row in a.index.tolist():
            
            # if the value in A is null
            if pd.isnull(a.loc[row, column]):
                # then the corresponding value in B should also be null
                assert pd.isnull(b.loc[row, column]), "Element in A is null, but corresponding element in B is not"
                
            # the same logic works the other way
            if pd.isnull(b.loc[row, column]):
                
                assert pd.isnull(a.loc[row, column]), "Element in B is null, but corresponding element in A is not"

    
    
    
    

    return True
#------------------------------------------------------------------------------
#                               END OF FUNCTION
#------------------------------------------------------------------------------


a = pd.DataFrame(1, columns = ["A", "B"], index = [*range(100)])

b = pd.DataFrame(2, columns = ["A", "B"], index = [*range(100)])

df_value_comparison(a, b)




