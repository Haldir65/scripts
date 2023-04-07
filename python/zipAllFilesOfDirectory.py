
import os
from zipfile import ZipFile


## 1. walk all files undeer directory 
## 2. adding those files to an zip file
## 2.1 immediately after adding file to zip file ,remove it
## 3. we now have an zip file filled with all files in certain directory 
## 4. now unzip to another directory
## 5. we may have two identical directory


def do_zip(dir,destFile):
    with ZipFile(destFile,'w') as zip_object:
        for folder_name, sub_folder_name,file_names in os.walk(dir):
            for filename in file_names:
                filepath = os.path.join(folder_name,filename)
                zip_object.write(filepath,os.path.basename(filepath))
                # os.remove(filepath)
                # print("remove original file {0} success ".format(filepath))         
    if os.path.exists(destFile):
        print("zipped file {0} exists".format(destFile))         
    else:
        print("zipped file {0} not exists".format(destFile))            

def do_unzip(filename,storage_dir):
    my_zip = ZipFile(filename) # Specify your zip file's name here
    if not os.path.exists(filename):
        raise AssertionError("file not found")
    if not os.path.isdir(storage_dir):
        raise AssertionError("storage dir is not an directory")
    for file in my_zip.namelist():
        print("found file {0} in zip file {1} ".format(file,filename))
        my_zip.extract(file, storage_dir) # extract the file to current folder if it is a text file

        # if my_zip.getinfo(file).filename.endswith('.txt'):
        #     my_zip.extract(file, storage_path) # extract the file to current folder if it is a text file





if __name__ == '__main__':
    zipFileName = 'resources/somefile.zip'
    fromDir = 'resources/directory1'
    toDir = 'resources/directory2'
    if not os.path.exists(fromDir):
        os.mkdir(fromDir)
    if not os.path.exists(toDir):
        os.mkdir(toDir)    
    do_zip(dir= fromDir,destFile= zipFileName)
    print("1 . zipping file complete normally \n")
    do_unzip(filename= zipFileName,storage_dir=toDir)
    print("2 . unzip file complete normally \n ")

    print("3 . everything went well \n ")

    ## du -sh by default show occupied dish size , not sum of all content's size as we expected


    ##➜ ls -goR directory1 | awk '{sum += $3} END{print sum}'
    # 614536

    # scripts/python/resources on  master [!?] via 🐍 3.11.2 via python
    # ➜ ls -goR directory2 | awk '{sum += $3} END{print sum}'
    # 614536

    # scripts/python/resources on  master [!?] via 🐍 3.11.2 via python
    # ➜ du -sh directory1
    # 620K	directory1

    # scripts/python/resources on  master [!?] via 🐍 3.11.2 via python
    # ➜ du -sh directory2
    # 628K	directory2






    # res = await asyncio.gather(*coros, return_exceptions=True)
    # asyncio.get_event_loop().run_until_complete(ht2())
