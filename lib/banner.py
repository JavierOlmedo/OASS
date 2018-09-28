import os
from lib.colors import Colors

VERSION = "1.0"

def banner():
    os.system("clear")
    print(Colors.BOLD +
    """
                    ________      _____    _________ _________
                    \_____  \    /  _  \  /   _____//   _____/
                     /   |   \  /  /_\  \ \_____  \ \_____  \ 
                    /    |    \/    |    \/        \/        \\
                    \_______  /\____|__  /_______  /_______  /
                            \/         \/        \/        \/     
                                                              v""" + VERSION + """
                                                                       
                ============ [OWASP Automatic Scan Script] ============
                               Made with ❤️  in Spain                          
                       
                ======= Javier Olmedo - https://hackpuntes.com ========
                [*] Facebook: https://facebook.com/hackpuntes       [*]
                [*] Twitter:  https://twitter.com/jjavierolmedo     [*]
                [*] LinkedIn: https://linkedin.com/in/jjavierolmedo [*]
                [*] GitHub:   https://github.com/JavierOlmedo       [*]
                =======================================================
    """ + Colors.DEFAULT)