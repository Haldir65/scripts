
import os,platform
import shutil
from color_print import _red,_green,_yellow,_blue

def is_windows():
    return platform.system() == 'Windows'

def sum_dir_size_in_bytes(abs_dir_path):
    isWindows = is_windows()
    if not os.path.exists(abs_dir_path):
        _red('dir path for {0} sum_dir_size_in_bytes not exists'.format(abs_dir_path))
        return 0
    elif not os.path.isdir(abs_dir_path):
        _red('dir path for {0} sum_dir_size_in_bytes is not dir'.format(abs_dir_path))
        return 0
    total_size = 0
    start_path = abs_dir_path # To get size of current directory
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            if( isWindows and len(fp)>260):
                fp = r"\\?\%s" % os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size 

def _delete_folder_and_return_size(dir_path):
    isWindows = is_windows()
    if(os.path.exists(dir_path) and os.path.isdir(dir_path)):
        dir_size = (sum_dir_size_in_bytes(dir_path))
        formateted = "{:.2f}".format(dir_size/1024/1024)
        _green('prepare to rmtree of dir {0} {1} \n whose occupied file size is {2} MB \n'.format(os.linesep,dir_path,formateted))
        if(isWindows and len(dir_path) > 10):
            ## https://burgaud.com/path-too-long/#maximum-path-length-limitation
            ## windows max filename length is 260, beyond that ,file not found 
            _yellow('beware file name {0} \n length exceed    currently we are at {1} '.format(dir_path,len(dir_path)))
            ext_path = r"\\?\%s" % dir_path
            shutil.rmtree(ext_path)
        else:
            shutil.rmtree(dir_path)
        return dir_size
    else:
        return 0 


def maybe_delete_build_dir(dirpath):
    app_buil_dir = os.path.join(dirpath,'app/build')
    _gradle_folder = os.path.join(dirpath,'.gradle')
    _cxx_folder = os.path.join(dirpath,'.cxx')
    app_build_size = _delete_folder_and_return_size(app_buil_dir)
    gradle_folder_size = _delete_folder_and_return_size(_gradle_folder)
    cxx_foler_size = _delete_folder_and_return_size(_cxx_folder)
    total_size = app_build_size + gradle_folder_size + cxx_foler_size
    formateted = "{:.2f}".format(total_size/1024/1024)
    _blue('deleted folder size for \n{0}  and\n {1} \n is {2}'.format(app_buil_dir,_gradle_folder,formateted))
    return total_size
   


def collecting_all_dirs():
    pwd = os.getcwd()
    all_dirs = [f for f in os.listdir(pwd) if os.path.isdir(os.path.join(pwd,f))]
    total_size = 0
    for dir in all_dirs:
        # _green("dir {0} \n".format(os.path.join(pwd,dir)))
        size = maybe_delete_build_dir(os.path.join(pwd,dir))
        if size:
            total_size+=size
    if total_size>0:
        _blue('all done , will free size {:.2f} MB '.format(total_size/1024/1024))
    else:
        _green(' all done , non is detected ')



def _walk_all_possible_directory():
    pwd = os.getcwd()
    results = []
    for root, dirs, files in os.walk(pwd, topdown=False):
        for name in dirs:
            split_dir = name.split(os.sep)
            if 'build' in split_dir or '.gradle' in split_dir or '.cxx' in split_dir:
                # _red('name is {0} '.format(os.path.join(root,name)))
                results.append(os.path.join(root,name))
                # print(os.path.join(root, name))
    total_size = 0
    for d in results:
        total_size+=_delete_folder_and_return_size(d)
    if total_size>0:
        formateted = "{:.2f}".format(total_size/1024/1024)
        _green('in total , we remove folder size  {0} Mb'.format(formateted))
    else:
        _green('no folder has been deleted {0} '.format(len(results)))    





def main():
    on_windows = is_windows()
    if on_windows:
        _yellow("be cautious , we are on windows , max length for file name must not exceed 260 .")
    _walk_all_possible_directory()
    # collecting_all_dirs()



if __name__ == "__main__":
    main()

