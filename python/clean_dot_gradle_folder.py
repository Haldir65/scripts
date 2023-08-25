# -*- coding: utf-8 -*-
import os
import time,datetime,platform,shutil
from color_print import _red,_green,_yellow,_blue
from io_utility import write_list_to_file_override,write_list_to_file_append

EXPIRED_DAYS = 30
READL_DELETE = True
LEAVE_RESULT = False


def is_windows():
    return platform.system() == 'Windows'

def clean_via_walk(start_path,expired_days = EXPIRED_DAYS):
    windows = is_windows()
    resultFiles = []
    resultDirs = []
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            if( windows and len(fp)>260):
                fp = r"\\?\%s" % os.path.join(path, f)
            #total_size += os.path.getsize(fp)
            if file_not_been_accessed_for_days(filepath= fp, dtime=expired_days):
                resultFiles.append(fp)
        for d in dirs:
            fp = os.path.join(path, d)
            if( windows and len(fp)>260):
                fp = r"\\?\%s" % os.path.join(path, f)
            #total_size += os.path.getsize(fp)    
            if file_not_been_accessed_for_days(filepath= fp, dtime=expired_days):
                resultDirs.append(fp)
    total_file_size = 0         
    total_folder_size = 0    
    for f in resultFiles:
        _blue("found file {0} not access for {1} days".format(f,expired_days))
        total_file_size += os.path.getsize(f)
        if READL_DELETE:
            os.remove(f)
        
    for f in resultDirs:
        _yellow("found directory {0} not access for {1} days".format(f,expired_days))    
        if READL_DELETE and os.path.exists(f):
            total_folder_size += os.path.getsize(f)
            shutil.rmtree(f)

    if LEAVE_RESULT:        
        result_file = "unused_files.txt"
        result_dir = "unused_dirs.txt"
        write_list_to_file_override(file_path=result_file,lines=resultFiles)    
        write_list_to_file_override(file_path=result_dir,lines=resultDirs)    

    _green("total file size = {0} MB".format(round(total_file_size/1024/1024,2)))
    _green("total folder size = {0} MB".format(round(total_folder_size/1024/1024,2)))


 
# 递归删除某个目录下所有过期文件
# expiredTime expressed in day
#
def cleanfile(path,expiredTime):
    for obj in os.listdir(path):
        objpath = os.path.join(path,obj)
        if os.path.isfile(objpath):
            delExpiredfile(objpath,expiredTime)
        elif os.path.isdir(objpath):
            cleanfile(objpath,expiredTime)
 
sum_size = 0


def file_not_been_accessed_for_days(filepath,dtime):
    expiredsec =  dtime * 24 * 3600
    stat_result =  os.stat(filepath)
    atime =  int(stat_result.st_atime)
    ntime = time.time()
    if (ntime - atime) > expiredsec:
        return True
    else:
        return False

def delExpiredfile(filepath,expiredTime):
    expiredsec =  expiredTime * 24 * 3600
    stat_result =  os.stat(filepath)
    atime =  int(stat_result.st_atime)
    ntime = time.time()
    file_size = os.path.getsize(filepath)/(1024*1024)
    if (ntime-atime)>expiredsec :
        try:
            global sum_size
            sum_size += file_size
            atime_str = datetime.datetime.fromtimestamp(atime).strftime('%Y-%m-%d %H:%M:%S')
            multiliner = """
        filepath = {0}
        filesize = {1}MB
        last access time = {2}  
        sum up to {3}MB
            """.format(filepath,round(file_size), atime_str,round(sum_size,2))
            _green(multiliner)
            # print(filepath, time.strftime("%m/%d/%y", time.localtime(atime)))
            # os.remove(filepath)
        except Exception as e:
            print(e)
    else:
        return False 
    

if __name__ == '__main__':
    path = os.path.expanduser('~')+"/.gradle/caches"
    # cleanfile(path, 14)
    clean_via_walk(start_path= path,expired_days=EXPIRED_DAYS)


    ## du -sh * | sort -n 
    ## sort folder by size 