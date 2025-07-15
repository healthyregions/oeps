from datetime import datetime
import pandas as pd
import numpy as np
import os
import re

import matplotlib.pyplot as plt

tables_folder = '../backend/oeps/data/tables/'

date_vars = ['AnyPdmpDt', 'AnyPdmphDt', 'OpPdmpDt', 'MsAcPdmpDt', 'ElcPdmpDt', 
             'AnyGslDt', 'GslArrDt', 'AnyNalxDt', 'NalxPrStDt', 'NalxPresDt']
fr_vars = ["AnyPdmpFr", 'AnyPdmphFr', 'OpPdmpFr', 'MsAcPdmpFr', 'ElcPdmpFr',
           'AnyGslFr', 'GslArrFr', 'AnyNalxFr', 'NalxPrStFr', 'NalxPresFr']

date_var_dict = {date_var:fr_var for date_var, fr_var in zip(date_vars, fr_vars)}

def get_table_sources(variable):
    '''Find all table sources containing a specific variable'''
    rv = []
    for table in os.listdir(tables_folder):
        file = tables_folder + table
        if any(pd.Series(variable).isin(pd.read_csv(file).columns)):
            rv.append(table)
    
    return rv

def get_dfs(table_sources, variables):
    """Given a list of tables, grab some slightly cleaned versions of those
    tables"""
    dfs = []
    for table in table_sources:
        df = pd.read_csv(tables_folder + table)
        df = df.set_index("HEROP_ID")
        df = df.sort_index()
        
        df = df

        dfs.append(df)
    
    return dfs

def column_has_impossible_date(series, year):
    """Given a pd.Series of dates and a specific year, return True if any
    of the dates are strictly *after* that year, and False otherwise."""
    if any(pd.to_datetime(series) > str(int(year)+1)):
        return True
    return False

def mask_future_dates(date_series, year):
    '''Given a pandas series of datetimes and a year,
    remove any datetimes that postdate the year.
    
    e.g. given the year 2016, 5/3/2017 will be removed
    but 12/29/2016 will not.'''
    
    end_date = datetime(int(year) + 1, 1, 1)    
    remaining_seconds = (end_date) - pd.to_datetime(date_series)
    
    mask = remaining_seconds.apply(lambda x: x.total_seconds()) < 0
    
    rv = date_series.copy()
    rv[mask] = np.NaN
    
    return rv

def calculate_fr_from_date(date_series, year):
    '''Given a pandas series of datetimes and a year,
    return an array of fractions of the year'''
    
    start_of_year = datetime(int(year), 1, 1)
    end_of_year = datetime(int(year) + 1, 1, 1)

    total_seconds = (end_of_year - start_of_year).total_seconds()
    remaining_seconds = (end_of_year - pd.to_datetime(date_series))\
        .apply(lambda x : x.total_seconds())

    rv = remaining_seconds / total_seconds
    rv[rv > 1] = 1
    
    rv =rv.fillna(0)

    assert not any(rv < 0), "Negative return value in rv, masking failed."

    return rv

def clean_fr_and_date(df, year, date_fr_dict, present_vars):
    '''Given a dataframe, a year, and a dictionary mapping
    date variables to fraction of a year variables, ensure 
    that the dataframe does not peer into the future by 
    masking future values with NAs and updating the 
    correspondent fraction of a year variables.'''

    # detangle ourselves from the initial df
    df = df.copy() 

    for column in present_vars:

        if column not in date_fr_dict: continue

        fr_column = date_fr_dict[column]

        print(f"Cleaning column {column} in year {year}")
        new_date_col = mask_future_dates(df[column], year)
        new_fr_col = calculate_fr_from_date(new_date_col, year)
        
        print(pd.concat( [df[column], new_date_col], axis=1 ))
        print(pd.concat( [df[fr_column], new_fr_col    ], axis=1 ))

        df[column] = new_date_col
        df[fr_column] = new_fr_col

    return df

def find_present_variables(df, variables):
    return list(set(df.columns).intersection(set(variables)))

def sanity_check(df, year):
    '''Given a dataframe a year, plot all datetimes present against
    the year.'''
    fig, ax = plt.subplots()

    for col in df.columns:
        to_plot = pd.to_datetime(df[col])

        ax.vlines(to_plot, 0, 1, color='black', alpha=0.1)
    
    ax.vlines(datetime(int(year) + 1, 1, 1), 0, 1, color='blue')
    
    return fig, ax

if __name__ == "__main__":
    tables = get_table_sources(date_vars + fr_vars)
    years = [table.split('-')[-1][:4] for table in tables]
    print(years)
    dfs = get_dfs(tables, date_vars + fr_vars)

    ## report current state of tables
    for df, table, year in zip(dfs, tables, years):
        present_variables = find_present_variables(df, date_vars + fr_vars)
        for variable in present_variables:
    
            if column_has_impossible_date(df[variable], year):
                print(f"Table {table} has impossible entry for variable {variable}")

    ## correct issues
    for i, (df, year) in enumerate(zip(dfs, years)):
        print('=' * 30)
        print(f'Correcting df {i} with year {year}')
        old_df = df.copy()
        present_variables = find_present_variables(df, date_vars + fr_vars)
        df = clean_fr_and_date(dfs[i], year, date_var_dict, present_variables)

        for col in present_variables:
            dfs[i][col] = df[col]

        dfs[i][present_variables] = df[present_variables]
        print(f"Masked a total of {pd.isna(old_df).sum() - pd.isna(df).sum()} new values for the dataframe from year {year}")

    print('Showing results graphs...')
    for i, _ in enumerate(dfs):
        fig, ax = sanity_check(dfs[i], years[i])
        ax.set_title(f"Dates present in data for year {years[i]}")
        plt.show()

    save_yn = input('Would you like to save the results? y/N?\t')
    if save_yn.lower() not in ['yes', 'y', 'ye', 'yeah']: exit(1)

    for df, table in zip(dfs, tables):
        df.to_csv(tables_folder + table, index=False)
    
