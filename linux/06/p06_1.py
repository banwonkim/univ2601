import os
import time
import sys #get argv
import stat
from datetime import datetime as dt

# if argc < 2
if len(sys.argv)<2:
    print('ERROR : argv < 2')
    exit()

for idx in range(1,len(sys.argv)):
    file_name=sys.argv[idx]
    print(f'[{file_name}]', end='\t')
    try:
        file_st=os.lstat(file_name)
    except FileNotFoundError:
        print('File not exist!')
        continue
    #File Type
    if stat.S_ISREG(file_st.st_mode):
        print('Normal File',end=', ')
    elif stat.S_ISDIR(file_st.st_mode):
        print('Directory',end=', ')
    elif stat.S_ISLNK(file_st.st_mode):
        print('Symbolic Link',end=', ')

    #Inode
    print('inode=', file_st.st_ino, end=', ')
    print('nlink=', file_st.st_nlink, end=', ')
    print('UID=', file_st.st_uid, end=', ')
    print('GID=', file_st.st_gid, end=', ')
    print('size=', file_st.st_size, end=', ')
    mtime = file_st.st_mtime
    print('mtime=', mtime, dt.fromtimestamp(mtime))


