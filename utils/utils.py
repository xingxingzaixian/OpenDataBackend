import zipfile
from pathlib import Path
from typing import List

def decompress_zip(zip_src: str, target_dir: str):
    r = zipfile.is_zipfile(zip_src)
    if r:   
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, target_dir)     
    else:
        print('This is not zip')
        

def compress_zip(target_file: Path, file_list: List[Path]):
    with zipfile.ZipFile(target_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_list:
            zf.writestr(file.name, file.read_text())