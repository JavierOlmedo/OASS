    '''
    if len(sys.argv[1:]) < 1:
        error("No arguments found!! Read how to use this tool and try again" + "\n")
    else:
        if sys.argv[1] != "-u":
            error("Please, read how to use this tool and try again" + "\n")
        else:
            if len(sys.argv[2:]) < 1:
                error("URL not valid" + "\n")
            else:
                target = sys.argv[2]

                if(isValidDomain(target)):
                    lib.globals.TARGET = target
                    try:
                        lib.globals.IP = socket.gethostbyname(target)
                    except:
                        error("No IP from " + lib.globals.TARGET)
                    success("TARGET " + target + " (" + lib.globals.IP + ")" + "\n")
                    owasp()
                else:
                    error(target + " is not a valid domain" + "\n")
    '''
def isTarget(url):
    global TARGET

    if (url[:8] != "https://" and url[:7] != "http://"):
        print(t() + colors.RED + "[!] You must insert http:// or https:// procotol" + colors.ENDC + "\n") 
    else:
        headers = { 'User-Agent': USERAGENT,
                    'Upgrade-Insecure-Requests': '1'}
        try:
            #r = requests.get(url)
            r = requests.get(url, headers=headers)

            if(r.status_code == 200):
                TARGET = url
                return True
            else:
                print(t() + colors.RED + "[!] This site is offline" + colors.ENDC + "\n")
                return False
        except:
             print(t() + colors.RED + "[!] An error has occurred" + colors.ENDC + "\n")
def createFolder():
    global PATHFOLDER
    global PATHDOWNLOADFILES

    nameFolder = TARGET.replace("https://", "")
    nameFolder = nameFolder.replace("http://", "")
    nameFolder = nameFolder.replace("/", "")

    pathDir = os.path.dirname(os.path.realpath(__file__))
    PATHFOLDER = pathDir + "/" + nameFolder
    PATHDOWNLOADFILES = PATHFOLDER + "/" + "files"

    if not os.path.exists(PATHFOLDER):
        try:
            os.makedirs(PATHFOLDER)
        except:
            print(t() + colors.RED + "[!] Error in make folder!!" + colors.ENDC + "\n")
            sys.exit(1)

    if not os.path.exists(PATHDOWNLOADFILES):
        try:
            os.makedirs(PATHDOWNLOADFILES)
        except:
            print(t() + colors.RED + "[!] Error in make folder!!" + colors.ENDC + "\n")
            sys.exit(1)
    createFileComments()
def createFileComments():
    global PATHFILECOMMENTS
    global PATHFOLDER

    PATHFILECOMMENTS = PATHFOLDER + "/" + "comments.txt"

    if not os.path.exists(PATHFILECOMMENTS):
        try:
            file = open (PATHFILECOMMENTS, 'r')
        except:
            file = open (PATHFILECOMMENTS, 'w')
            #print(t() + colors.RED + "[!] Error in make file comments!!" + colors.ENDC + "\n")
            #sys.exit(1)
    else:
        file = open (PATHFILECOMMENTS, 'w')