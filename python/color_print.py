## [python print with color](https://stackoverflow.com/a/65860612)
class colors:  # You may need to change color settings
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    BRIGHT_RED = '\033[1;31m'
    BRIGHT_GREEN = '\033[1;32m'
    BRIGHT_YELLOW = '\033[1;33m'
    BRIGHT_BLUE = '\033[1;34m'
    BRIGHT_MAGENTA = '\033[1;35m'
    BRIGHT_CYAN = '\033[1;36m'
    BRIGHT_WHITE = '\033[1;37m'
    ENDC = '\033[m'

def _red(str):
    print(colors.RED + str + colors.ENDC)

def _green(str):
    print(colors.GREEN + str + colors.ENDC)

def _yellow(str):
    print(colors.YELLOW + str + colors.ENDC)

def _blue(str):
    print(colors.BLUE + str + colors.ENDC)

def _magenta(str):
    print(colors.MAGENTA + str + colors.ENDC)

def _cyan(str):
    print(colors.CYAN + str + colors.ENDC)

def _white(str):
    print(colors.WHITE + str + colors.ENDC)

def _black(str):
    print(colors.BLACK + str + colors.ENDC)

def _bright_red(str):
    print(colors.BRIGHT_RED + str + colors.ENDC)

def _bright_green(str):
    print(colors.BRIGHT_GREEN + str + colors.ENDC)

def _bright_yellow(str):
    print(colors.BRIGHT_YELLOW + str + colors.ENDC)

def _bright_blue(str):
    print(colors.BRIGHT_BLUE + str + colors.ENDC)

def _bright_magenta(str):
    print(colors.BRIGHT_MAGENTA + str + colors.ENDC)

def _bright_cyan(str):
    print(colors.BRIGHT_CYAN + str + colors.ENDC)

def _bright_white(str):
    print(colors.BRIGHT_WHITE + str + colors.ENDC)