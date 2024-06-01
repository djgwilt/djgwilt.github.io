from zipfile import ZipFile
from glob import glob
from os import mkdir, path, remove
import shutil
import os


for zip in glob("*.zip"):
    with ZipFile(zip, 'r') as zip_ref:
        out = zip.replace(".zip","")
        if not path.exists(out):
            mkdir(out)
        zip_ref.extractall(out)

print("Move extracted data to root? y/n")
print("If you move, it will overwrite existing folders")
rem = input().lower()
if rem == "y":
    for zip in glob("*.zip"):
        src = zip.replace(".zip","")
        subs = glob(f"{src}/*")
        for sub in subs:
            sub = os.path.basename(sub)
            if os.path.exists(sub):
                shutil.rmtree(sub)
            shutil.copytree(f"{src}/{sub}", sub)
    

print("Remove zip files? y/n")
rem = input().lower()
if rem == "y":
    filelist = glob(path.join("*.zip"))
    for f in filelist:
        remove(f)
