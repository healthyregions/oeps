import os
import requests
from datetime import datetime

from oeps_backend.utils import LOCAL_DATA_DIR

## CHANGESET is the specific commit on the GeoDaCenter/opioids-policy-scan repo
## to target for the version of files we need to work from.
## 115989bd1f6706e2b225da9a88c27c5e34e42692 is the version 1.0 release of the main branch.
CHANGESET = "115989bd1f6706e2b225da9a88c27c5e34e42692"

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
    ],
    "csv": [
        "Access01_C.csv",
        "Access01_S.csv",
        "Access01_T.csv",
        "Access01_Z.csv",
        "Access02_C.csv",
        "Access02_S.csv",
        "Access02_T.csv",
        "Access02_Z.csv",
        "Access03_C.csv",
        "Access03_S.csv",
        "Access03_T.csv",
        "Access03_Z.csv",
        "Access04_C.csv",
        "Access04_S.csv",
        "Access04_T.csv",
        "Access04_Z.csv",
        "Access05_C.csv",
        "Access05_S.csv",
        "Access05_T.csv",
        "Access05_Z.csv",
        "Access06_C.csv",
        "Access06_S.csv",
        "Access06_T.csv",
        "Access06_Z.csv",
        "Access07_T.csv",
        "Access07_Z.csv",
        "BE01_C.csv",
        "BE01_S.csv",
        "BE01_T.csv",
        "BE01_Z.csv",
        "BE02_RUCA_C.csv",
        "BE02_RUCA_T.csv",
        "BE02_RUCA_Z.csv",
        "BE03_C.csv",
        "BE03_S.csv",
        "BE03_T.csv",
        "BE03_Z.csv",
        "BE04_C.csv",
        "BE05_C.csv",
        "BE05_S.csv",
        "BE05_Z.csv",
        "BE06_NDVI_C.csv",
        "BE06_NDVI_S.csv",
        "BE06_NDVI_T.csv",
        "BE06_NDVI_Z.csv",
        "BE07_C.csv",
        "BE07_S.csv",
        "COVID01_C.csv",
        "COVID01_S.csv",
        "COVID02_C.csv",
        "COVID02_S.csv",
        "COVID03_C.csv",
        "COVID03_S.csv",
        "COVID04_C.csv",
        "COVID04_S.csv",
        "DS01_C.csv",
        "DS01_S.csv",
        "DS01_T.csv",
        "DS01_Z.csv",
        "DS02_T.csv",
        "DS03_C.csv",
        "DS03_T.csv",
        "DS03_Z.csv",
        "DS04_C.csv",
        "DS04_S.csv",
        "DS04_T.csv",
        "DS04_Z.csv",
        "DS05_C.csv",
        "DS05_S.csv",
        "DS05_T.csv",
        "DS05_Z.csv",
        "DS06_C.csv",
        "DS06_S.csv",
        "DS06_T.csv",
        "DS06_Z.csv",
        "EC01_C.csv",
        "EC01_S.csv",
        "EC01_T.csv",
        "EC01_Z.csv",
        "EC02_C.csv",
        "EC02_S.csv",
        "EC02_T.csv",
        "EC02_Z.csv",
        "EC03_C.csv",
        "EC03_S.csv",
        "EC03_T.csv",
        "EC03_Z.csv",
        "EC04_C.csv",
        "EC04_S.csv",
        "EC04_T.csv",
        "EC05_C.csv",
        "EC05_S.csv",
        "EC05_T.csv",
        "EC05_Z.csv",
        "Health01_C.csv",
        "Health01_S.csv",
        "Health02_C_Mortality.csv",
        "Health02_S_Mortality.csv",
        "Health02_S_Prevalence.csv",
        "Health03_C.csv",
        "Health03_S.csv",
        "Health03_T.csv",
        "Health04_C.csv",
        "Health04_S.csv",
        "PS01_2016_C.csv",
        "PS02_2017_C.csv",
        "PS03_2017_S.csv",
        "PS04_2018_S.csv",
        "PS05_2017_S.csv",
        "PS06_2019_S.csv",
        "PS07_2018_S.csv",
        "PS08_2019_S.csv",
        "PS09_2017_S.csv",
        "PS11_S.csv",
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