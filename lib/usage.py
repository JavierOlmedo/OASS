from lib.colors import Colors

def usage():
	print(Colors.BOLD + """
	EXAMPLE:
		-u [REQUIRED] Specify the URL of target
		python3 oass.py [PATH]
        
		-o [OPTIONAL] Output folder
		python3 oass.py [PATH] -o [OUTPUT]
	""" + Colors.DEFAULT)