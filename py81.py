import sys
import os
import stat
import time


def get_fmode_str(mode):
    if stat.S_ISDIR(mode): ftype = 'd(dir)'  # 디렉토리
    elif stat.S_ISLNK(mode): ftype = 'l(link)'  # 심볼릭 링크
    elif stat.S_ISREG(mode): ftype = 'f(file)'  # 일반 파일
    elif stat.S_ISFIFO(mode):
        ftype = 'p'  # 파이프
    elif stat.S_ISSOCK(mode):
        ftype = 's'  # 소켓
    elif stat.S_ISCHR(mode):
        ftype = 'c'  # 캐릭터 디바이스
    elif stat.S_ISBLK(mode):
        ftype = 'b'  # 블록 디바이스
    else:
        ftype = '?'  # 알 수 없음
    return ftype
if len(sys.argv)<2:
    argv='.'
    #print('[MSG] NO ARGV')
    #exit(1)
else: argv=sys.argv[1]
f_dir=argv

with os.scandir(f_dir) as f_list:
    for f in f_list:
        f_ls=os.lstat(f.path)
        #print(f_ls, '>>>>>>>>>>>>>>>>')
        f_mode=stat.filemode(f_ls.st_mode)
        f_fmode=get_fmode_str(f_ls.st_mode)
        
        mod_time_struct = time.localtime(f_ls.st_mtime)
        f_time_s=time.strftime("%Y-%m-%d %H:%M:%S", mod_time_struct)
        print(f'type:{f_fmode} mode:{f_mode} nlink:{f_ls.st_nlink} UID:{f_ls.st_uid} GDI:{f_ls.st_gid} size:{f_ls.st_size} mtime:{f_time_s} fname:{f.name}')
