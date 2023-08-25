## [python print with color](https://stackoverflow.com/a/65860612)
class colors: # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def _red(str):
    print(colors.RED + str + colors.ENDC)

def _green(str):
    print(colors.GREEN + str + colors.ENDC)

def _yellow(str):
    print(colors.YELLOW + str + colors.ENDC)

def _blue(str):
    print(colors.BLUE + str + colors.ENDC)