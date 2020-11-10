#!/usr/bin/python3

import sys,os
def List(dir):
	path = os.path.abspath(dir)
	print(path)
	items = os.listdir(dir)
	print(items)
	print('='*50)
	for item in items:
		fullpath = path + '/' +  item
		if os.path.isfile(fullpath):
			print(fullpath + 'is a file')
		else:
			os.path.isdir(fullpath):
			print(fullpath + 'is a folder')
		else:
			print('Unknown !!!')

def amin():
	List(sys.argv[1])
if __name__ == '__main__:'
	main()
