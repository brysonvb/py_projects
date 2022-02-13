#
# Unzip PoC
#
#
# Usage:
# Copy into folder with ZIP files, script with walk the directory
# detect ZIP files, and decompress using multi-processor
#
# Notes:
#
# Known Issues:
# 
#


import locale
locale.setlocale(locale.LC_ALL, "")

import collections         #dictionary
import os                  #OS access
import multiprocessing     #multi-processing to utilize multi-core systems
import time                #system time
import queue               #queue types
import zipfile

path = "c:\\test"

def main():
    global path
    st_time = time.time()
    
    data = collections.defaultdict(list)
    print("Processing Directory...")
    data = process_dir(path)
    files = []
    print("\nValid Files: " + str(len(data)))
    print("Procesing ZIP files...")
    if data:
        for key in data:
            fn = "".join(data[key])
            z = zipfile.ZipFile(fn,"r")
            zfiles = []
            for zfile in z.namelist():
                zfiles.append(zfile)
            files.append((fn,zfiles))
            z.close()

##    if files:
##        for fn in files:
##            z = zipfile.ZipFile(fn[0],"r")
##            for zfiles in fn[1]:
##                z.extract(zfiles,path)
##            z.close()
            
    if files:    # Extract zip files using multiple cores
        pool = multiprocessing.Pool()
        pool.map_async(check_one_item, files)
        pool.close()
        pool.join()
##
##
##    print("Creating Directory Structure...")
##    if starget:
##        for filename in starget:
##            path = filename[:filename.rfind("\\")]
##            if path != cpath:
##                make_path(filename)
##                cpath = path

    en_time = time.time()        
    print("Total Time: " + str(en_time-st_time))
    print("DONE!")

def process_dir(path):
    
    data = collections.defaultdict(list)

    for root, dirs, files in os.walk(path):
        for filename in files:
            fullname = os.path.join(root, filename)
            try:
                key = (os.path.getsize(fullname), filename)
            except EnvironmentError:
                print("Env Error: "+fullname)
                continue
            if key[0] == 0:
                print("Zero Size: "+fullname)
                continue
            if zipfile.is_zipfile(filename):
                data[key].append(fullname)
                print("Zip: ", fullname)
    return data


def check_one_item(files):
    global path
    result = []
    z = zipfile.ZipFile(files[0],"r")
    for zfiles in files[1]:
        z.extract(zfiles,path)
    z.close()
    return


def print_result(results):
     print(results,"\n")

if __name__ == "__main__":
    main()

