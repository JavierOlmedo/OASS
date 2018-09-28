from lib.colors import Colors

def usage():
	print(Colors.BOLD + """
	EXAMPLE:
		-p [REQUIRED] Specify the PATH of source code
		python3 s2d.py [PATH]
        
		-o [OPTIONAL] Output folder
		python3 s2d.py [PATH] -o [OUTPUT]
	""" + Colors.DEFAULT)