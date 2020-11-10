#!/usr/bin/python3

import os,sys
def List(dir):
	filenames = os.listdir(dir)
	print(filenames)
	for element in filenames:
		print("Name of object: ",element)
		path = os.path.join(dir,element)
		print("Object Path: ",path)
		print('+' * 70)
def main():
	List(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/python/working-with-files-folders-with-OS# ./contents-with-path-relorabsolute-ofdirectory-location.py /root/python/
# ['Directory-Traversal', 'working-with-files-folders-with-OS']
# Name of object:  Directory-Traversal
# Object Path:  /root/python/Directory-Traversal
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Name of object:  working-with-files-folders-with-OS
# Object Path:  /root/python/working-with-files-folders-with-OS
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
