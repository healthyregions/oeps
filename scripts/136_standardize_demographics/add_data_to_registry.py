### Author: Ashlynn Wimer
### Date: 8/18/2025
### About: This script adds the collected R data to the registry, and then
###        updates the registry itself.
###        **Note that this script _must_ be in oeps/backend to run.**

from oeps.clients.registry import Registry, TableSource
import pandas as pd
from os import listdir
from pathlib import Path
import warnings
import numpy as np
### Constants -------

DATA_PATH = '../scripts/136_standardize_demographics/exported/'
TABLE_SOURCE_PATH = "oeps/data/tables/"
REGISTRY_PATH = "oeps/data/variables"

COLUMNS_TO_REMOVE = ['Age18_64', 'Age0_4', 'Age5_14', 'TotPop10', 
                     'UrbPop', "Age15_19", "Age20_24", "Age45_54", "Age55_59",
                     "Age60_64", "Age45_49", "Age50_54", "A15_24P", "NoHsP",
                     "AgeOv65"]

# INCOMING_VALID_NAMES = ["HEROP_ID", 'TotPop', "Ovr16", "Ovr16P", "Ovr18", "Ovr18P",
#                         "Ovr21", "Ovr21P", "Ovr65", "Ovr65P", "Age15_44", "Age15_44P",
#                         "MedAge", "MaleP", "FemP", "SRatio", "SRatio18", "SRatio65",
#                         "BlackE", "BlackP", "WhiteP", "WhiteE", "HispP", "HispE",
#                         "AmIndP", "AmIndE", "AsianP", "AsianE", "PacIsP", "PacIsE",
#                         "OtherP", "OtherE", "TwoRaceP", "TwoRaceE"]

# NEW = BlackE, WhiteE, HispE, AmIndE, AsianE, PacIsE, OtherE, TwoRaceE

# ['HisPop', 'SomeCollege', 'Ovr18', 'PacIsPop', 'HispPop', 'Age15_44', 
# 'TotPop', 'BlackPop', 'HispP', 'Ovr16', 'HEROP_ID', 'FIPS', 'GEOID', 'Ovr65',
# 'trtid10', 'HispE', 'PacIsP', 'WhiteP', 'Ovr65P', 'AmIndPop', 'Unnamed: 0', 
# 'FemaleP', 'AsianP', 'BlackP', 'Age15_44P', 'WhitePop', 'OtherP', 'TwoPlsE', 
# 'Ovr21', 'TwoPlsP', 'AmIndP', 'AsianPop']

def fix_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    '''Coerce float columns to integers.'''
    
    cols_to_coerce = ['TotPop', 'WhiteE', 'BlackE', 'AsianE', 'HisE', 'PacIsE',
                      'OtherE', 'TwoRaceE']
    
    df = df.copy()
    running_mask = pd.Series([False for _ in range(df.shape[0])])
    for col in cols_to_coerce:
        if not col in df.columns: continue
        mask = (df[col].isna()) | (df[col] == np.inf)
        running_mask = mask | running_mask
        pd.options.mode.use_inf_as_na = True
        df[col] = df[col].fillna(np.nan)
        pd.options.mode.use_inf_as_na = False
        df[col] = df[col].round(0).astype(np.int64)

    print(df.loc[running_mask, [col for col in cols_to_coerce if col in df.columns]])
    
    return df

INVALID_INCOMING_KEYS = ['trctid10', 'FIPS', 'GEOID']

RENAMER = dict(NoHsP = "EduNoHsP",      WhitePop = "WhiteE",
               BlackPop = "BlackE",     HispPop = "HisE",
               AmIndPop = "AmIndE",     AsianPop = "AsianE",
               PacIsPop = "PacIsE",     OtherPop = "OtherE",
               TwoRacePop = "TwoRaceE", SomeCollege = "SomeCollegeP",
               FemaleP = "FemP",        HisPop = "HisE", 
               TwoPlsP = "TwoRaceP",    HispE  = "HisE",
               TwoPlsE = "TwoRaceE",    Und18P = "Children") 

exported_data = listdir(DATA_PATH)

### Helpers -------

def rename_columns(df: pd.DataFrame, full_renamer=RENAMER) -> pd.DataFrame:
    '''Given a staged dataframe, rename columns within the dataframe to ensure
    maximum validity and asalignment with the registry.'''

    renamer = {k:v for k, v in full_renamer.items()
               if k in df.columns}
    
    if renamer != {}: df = df.copy().rename(columns=renamer)

    return df

def validate_incoming(df: pd.DataFrame) -> pd.DataFrame:
    '''Given the incoming dataframe, ensure that all columns within the
     data frame are valid, that HEROP_ID is the only key present, and also 
      enforce renaming as needed (if possible). 
      
      Returns a copy of the dataframe which has been validated, or throws an error.'''
    
    assert "HEROP_ID" in df.columns, f'Incoming dataset appears to be missing HEROP_ID column.'

    present_invalid_keys = [invalid_key for invalid_key in INVALID_INCOMING_KEYS
                            if invalid_key in df.columns]
    if present_invalid_keys != []:
        warnings.warn('Detected invalid key in incoming table; removing.')
        df = df.copy().drop(columns=present_invalid_keys)
    
    renamer = {k:v for k,v in RENAMER.items() 
               if k in df.columns}
    
    if renamer != {}: df = df.copy().rename(columns=renamer)

    if not all(column in INCOMING_VALID_NAMES for column in df.columns):
        invalid = [column for column in df.columns if column not in INCOMING_VALID_NAMES]
        raise ValueError(f"Invalid columns {invalid} present in dataframe with a HEROP_ID {df.HEROP_ID[0]}")
    
    return df


def remove_dead_columns(df: pd.DataFrame) -> pd.DataFrame:
    '''Given a dataframe, remove all columns which are deprecated.
    Return a copy of the dataframe without this columns.'''

    dead_columns_present = [column for column in df.columns 
                            if column in COLUMNS_TO_REMOVE]
    df = df.copy().drop(columns=dead_columns_present)

    return df

def update_registry(registry, new_data, data_table_name):
    '''Update the registry to ensure that the current data table
    is accurately captured by the registry. Does not delete *variables* from
    the registry.'''

    # TODO: implement this function. like, for realsies

    return registry

### Logic -------

if __name__ == "__main__":

    registry = Registry()
    needs_renamed = []
    for datafile in exported_data:

        # guess scale and year
        scale, year = tuple(datafile.split('-')[:2])
        if '.' in year: year = year.split('.')[0]
        if scale == "states": scale = "state"

        # read in data
        table_source = TableSource(name=f"{scale}-{year}", with_data=True, 
                                   registry=registry)

        # fix known preexistent weirdness in data tables
        if table_source.name in ['county-1980', 'state-1980', 'county-1990']:
            table_source.df['TotPop'] = table_source.df.TotPop.round(0)
            table_source.df['TotUnits'] = table_source.df.TotUnits.round(0)
            table_source.df['Age15_44'] = table_source.df.Age15_44.round(0)

        incoming_data_loc = f'{DATA_PATH}/{datafile}'
        table_source.stage_incoming_csv(Path(incoming_data_loc))
        table_source.staged_df = rename_columns(table_source.staged_df, RENAMER)
        
        table_source.df = table_source.df.drop(
            columns=[col for col in table_source.df
                     if col in COLUMNS_TO_REMOVE])
        
        table_source.validate_incoming_csv()
        table_source.merge_incoming_csv()

        registry.sync_variable_table_sources(table_source)