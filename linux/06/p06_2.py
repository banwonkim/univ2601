import os
import time
import sys #get argv
import stat

# if argc < 3
if len(sys.argv)<3:
    print('ERROR : argv < 3')
    exit()

mod_str=sys.argv[1]
mod=int(mod_str,8)
file=sys.argv[2]
file_st=os.stat(file)

mod_prev=oct(stat.S_IMODE(file_st.st_mode))
#print(f'{mod_str} -> {mod}')

os.chmod(file, mod)
print(f'Permission {mod_prev} -> {oct(mod)}')
# print(f'file mode : {file_st}')


#now=time.time()
