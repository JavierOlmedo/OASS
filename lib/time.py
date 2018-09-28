#!/usr/bin/python3

import time

def t():
	current_time = time.localtime()
	ctime = time.strftime('%H:%M:%S', current_time)
	return "["+ ctime + "]"