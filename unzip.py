import os
import glob
import patoolib
from pathlib import Path

# Unzips all tar files
def extract_tar(path):
    path_to_files = path
    print("2. Unzip TAR files ...")
    for item in glob.glob(path_to_files +'/*.tar'):
        dirpath = os.path.dirname(item)
        patoolib.extract_archive(item, outdir=dirpath)
        os.remove(item)
    return

# Unzips all bz2 files from the folders
def extract_bz2(path):
    path_to_files = path
    print("3. Extracting BZ2 files ...")
    for item in glob.glob(path_to_files + '/**/*.bz2', recursive=True):
        dirpath = os.path.dirname(item)
        patoolib.extract_archive(item, outdir=dirpath)
        os.remove(item)
    return
