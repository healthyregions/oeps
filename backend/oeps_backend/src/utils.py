import os
import requests
from glob import glob
from pathlib import Path

def get_path_or_paths(path_input, extension=None):

    if os.path.isdir(path_input):
        if extension:
            paths = glob(os.path.join(path_input, f"*.{extension}"))
        else:
            paths = glob(os.path.join(path_input))
    elif os.path.isfile(path_input):
        paths = [path_input]
    else:
        print('invalid path:', path_input)
        exit()
    
    return paths

def download_file_or_shapefile(url, out_dir):
    """ Takes an input url to a file and downloads it to specified dir.
    If that url points to a .shp file, attempt to download sidecars
    as well. Return only the path to the file from the original
    url. """

    if url.endswith(".shp"):
        urls = [
            url,
            url.replace(".shp", ".dbf"),
            url.replace(".shp", ".shx"),
            url.replace(".shp", ".prj"),
            url.replace(".shp", ".cpg"),
            url.replace(".shp", ".eee"),
        ]
    else:
        urls = [url]

    files = []
    for u in urls:
        name = u.split("/")[-1]
        response = requests.get(u, stream=True)
        if response.status_code == 200:
            out_path = Path(out_dir, name)
            print(f"    {u} --> {out_path}")
            with open(Path(out_dir, name), mode="wb") as file:
                for chunk in response.iter_content(chunk_size=10 * 1024):
                    file.write(chunk)
            files.append(out_path)

    return files[0]