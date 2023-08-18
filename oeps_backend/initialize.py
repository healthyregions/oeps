import os
import requests
from datetime import datetime

from oeps_backend.utils import LOCAL_DATA_DIR

## CHANGESET is the specific commit on the GeoDaCenter/opioids-policy-scan repo
## to target for the version of files we need to work from.
## 115989bd1f6706e2b225da9a88c27c5e34e42692 is the version 1.0 release of the main branch.
## 0deb3b54169268bfbeb3e53fdc7e0df1579a7922 corresponds to the commit immediately before 
## PR #66 to archive v1.1 datasets and promote v2.0 datasets, and should be changed in the
## future.
CHANGESET = "0deb3b54169268bfbeb3e53fdc7e0df1579a7922"

## BASE_URL is the raw url for github content based on the CHANGESET provided,
## down to the data_final directory. All DOWNLOAD_FILES paths are relative to this url.
BASE_URL = f"https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/{CHANGESET}/data_final/"

## This dictionary holds local directory paths as keys with the list of
## remote files, relative to BASE_URL that should be downloaded into that local directory
DOWNLOAD_FILES = {
    "shp": [
        "geometryFiles/county/counties2018.dbf",
        "geometryFiles/county/counties2018.prj",
        "geometryFiles/county/counties2018.shp",
        "geometryFiles/county/counties2018.shx",
        "geometryFiles/state/states2018.dbf",
        "geometryFiles/state/states2018.prj",
        "geometryFiles/state/states2018.shp",
        "geometryFiles/state/states2018.shx",
        "geometryFiles/tract/tracts2018.dbf",
        "geometryFiles/tract/tracts2018.prj",
        "geometryFiles/tract/tracts2018.shp",
        "geometryFiles/tract/tracts2018.shx",
        "geometryFiles/zcta/zctas2018.dbf",
        "geometryFiles/zcta/zctas2018.prj",
        "geometryFiles/zcta/zctas2018.shp",
        "geometryFiles/zcta/zctas2018.shx",
        "geometryFiles/tl_2010_county/counties2010.dbf",
        "geometryFiles/tl_2010_county/counties2010.prj",
        "geometryFiles/tl_2010_county/counties2010.shp",
        "geometryFiles/tl_2010_county/counties2010.shx",
        "geometryFiles/tl_2010_state/states2010.dbf",
        "geometryFiles/tl_2010_state/states2010.prj",
        "geometryFiles/tl_2010_state/states2010.shp",
        "geometryFiles/tl_2010_state/states2010.shx",
        "geometryFiles/tl_2010_tract/tracts2010.dbf",
        "geometryFiles/tl_2010_tract/tracts2010.prj",
        "geometryFiles/tl_2010_tract/tracts2010.shp",
        "geometryFiles/tl_2010_tract/tracts2010.shx", 
#        "geometryFiles/tl_2010_zcta510/zctas2010.dbf",
#        "geometryFiles/tl_2010_zcta510/zctas2010.prj",
#        "geometryFiles/tl_2010_zcta510/zctas2010.shp",
#        "geometryFiles/tl_2010_zcta510/zctas2010.shx",                               
    ],
    "csv": [
        "v2.0/tables/C_1980.csv",
        "v2.0/tables/C_1990.csv",
        "v2.0/tables/C_2000.csv",
        "v2.0/tables/C_2010.csv",
        "v2.0/tables/C_Latest.csv", 
        "v2.0/tables/S_1980.csv",
        "v2.0/tables/S_1990.csv",
        "v2.0/tables/S_2000.csv",
        "v2.0/tables/S_2010.csv",
        "v2.0/tables/S_Latest.csv",
        "v2.0/tables/T_1980.csv",
        "v2.0/tables/T_1990.csv",
        "v2.0/tables/T_2000.csv",
        "v2.0/tables/T_2010.csv",
        "v2.0/tables/T_Latest.csv",
        "v2.0/tables/Z_1980.csv",
        "v2.0/tables/Z_1990.csv",
        "v2.0/tables/Z_2000.csv",
        "v2.0/tables/Z_2010.csv",
        "v2.0/tables/Z_Latest.csv",
    ],
    "dictionaries": [
        "v2.0/dictionaries/S_Dict.xlsx",
        "v2.0/dictionaries/T_Dict.xlsx",
        "v2.0/dictionaries/Z_Dict.xlsx",
        "v2.0/dictionaries/C_Dict.xlsx",
    ],
    "metadata": [
        "metadata/HepC_rate.md",
        "metadata/Access_FQHCs_MinDistance.md",
        "metadata/Access_MentalHealth_MinDistance.md",
        "metadata/Access_MOUDs.md",
        "metadata/Access_OpioidUseTreatment.md",
        "metadata/Access_Pharmacies_MinDistance.md",
        "metadata/Access_SubstanceUseTreatment.md",
        "metadata/Acesss_Hospitals_MinDistance.md",
        "metadata/Age_2018.md",
        "metadata/AlcoholOutlets_2018.md",
        "metadata/COVID.md",
        "metadata/crosswalk.md",
        "metadata/Economic_2018.md",
        "metadata/ForeclosureRate.md",
        "metadata/GeographicBoundaries_2018.md",
        "metadata/GSL_2018.md",
        "metadata/Health_DrugDeaths.md",
        "metadata/Health_PCPs.md",
        "metadata/Historical_Methadone_point.md",
        "metadata/HomelessPop.md",
        "metadata/HouseholdType.md",
        "metadata/Housing_2018.md",
        "metadata/Internet_2019.md",
        "metadata/Jail variables_2017.md",
        "metadata/Jail-variables_2017.html",
        "metadata/Job_Categories_byIndustry_2018.md",
        "metadata/Job_Categories_byOccupation_2018.md",
        "metadata/MedExpan_2018.md",
        "metadata/MedExp_2019.md",
        "metadata/MedMarijLaw.md",
        "metadata/metadata-template.md",
        "metadata/NAL_2017.md",
        "metadata/NDVI.md",
        "metadata/OpioidIndicators.md",
        "metadata/Other_Demographic_2018.md",
        "metadata/Overlay.md",
        "metadata/Park_Cover.md",
        "metadata/PDMP_2017.md",
        "metadata/Prison variables_2016.md",
        "metadata/Prison-variables_2016.html",
        "metadata/PublicExpenditures.md",
        "metadata/Race_Ethnicity_2018.md",
        "metadata/Residential_Seg_Indices.md",
        "metadata/Rural_Urban_Classification_County.md",
        "metadata/Rural_Urban_Classification_T_Z.md",
        "metadata/SDOH_2014.md",
        "metadata/SVI_2018.md",
        "metadata/Syringe.md",
        "metadata/VetPop.md",
    ]
}

def download_fileset(dir_name, file_list):

    target_dir = os.path.join(LOCAL_DATA_DIR, dir_name)
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    print(f"getting {dir_name} data...")
    for f in file_list:
        f_url = BASE_URL + f
        f_name = f_url.split("/")[-1]
        target_file_path = os.path.join(target_dir, f_name)
        print(f"  --> {f_name}")
        r = requests.get(f_url, stream=True)
        with open(target_file_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

if __name__ == "__main__":

    start = datetime.now()
    for dir_name, file_list in DOWNLOAD_FILES.items():
        download_fileset(dir_name, file_list)
    print(f"completed in {datetime.now() - start}")