import os
import time
import sys
import signal

g_cpid=None
def handler(signo, frame):
    global g_cpid
    if g_cpid:
        print('time out, kill chld process')
        os.kill(g_cpid, signal.SIGTERM)
    #signal.alarm(0)
def command_get_sec():
    if len(sys.argv)<3:
        print('[Error] argv < 3')
        exit(1)
    return sys.argv[1], sys.argv[2:]
if __name__ == '__main__':
    sec, argv= command_get_sec()
    r,w=os.pipe()
    pid=os.fork()
    if pid==0: #child process
        os.close(r) #close unused file dsc
        write_fd=w
        os.dup2(write_fd, 1)
        try:
            os.execvp(argv[0], argv)
        except OSError:
            print(f'{arg}: command not found')
            os._exit(127)
        os.close(w)
        os._exit(1)

    elif pid>0:
        os.close(w)
        cpid,st = os.waitpid(pid, 0)
        if os.WIFEXITED(st):
            print(f'')
        signal.signal(signal.SIGALRM, handler) #?
        signal.alarm(sec)

