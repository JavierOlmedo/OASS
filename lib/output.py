from lib.functions import t
from lib.colors import Colors

def error(s):
    print(Colors.BOLD + Colors.RED + t() + " [ERROR] " + s + Colors.DEFAULT)