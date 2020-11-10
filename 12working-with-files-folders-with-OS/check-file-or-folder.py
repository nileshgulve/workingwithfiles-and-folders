#!/usr/bin/python3

import os,sys
def main():
	print(os.path.exists('wf/folder'))
	print(os.path.exists('wf/file0a'))
	os.path.exists('folder')
if __name__ == '__main__':
	main()
# Output:
# root@deb1:~/python/working-with-files-folders-with-OS# chmod 755 check-file-or-folder.py 
# root@deb1:~/python/working-with-files-folders-with-OS# ./check-file-or-folder.py 
# True
# False
# root@deb1:~/python/working-with-files-folders-with-OS# tree wf/
# wf/
# ├── file0a.txt
# └── folder

