import os
import signal
from datetime import datetime
def main():
    exit_code=None
    while True:
        line=input('mini$ ')
        line_arr=line.split()
        if len(line_arr)==0: continue
        arg,args=line_arr[0],line_arr[1:]
        match line_arr[0]:
            #case 'echo':
            #    print(','.join(args))
            #case 'pwd':
            #    pwd=os.getcwd()
            #    print(pwd)
            case 'status':
                print('last exit code: ',end='')
                if exit_code==None:
                    print('none')
                else:
                    print(exit_code)
            case 'help':
                print('''builtins: help, status, exit [code]
external commands: executed by fork + execvp + waitpid
unsupported: cd, pipe, redirection, background execution''')
            case 'date':
                now=datetime.now()
                print(f"{now.strftime('%Y. %m. %d.')} ({['월','화','수','목','금','토','일'][now.weekday()]}) {now.strftime('%H:%M:%S')}")
            case 'exit':
                if len(args)==0:
                    os._exit(0)
                try:
                    no=int(args[0])
                    os._exit(no)
                except ValueError:
                    print(f'{args[0]}: numeric argument required')
            case _:
                old_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
                pid=os.fork()
                if pid<0:
                    print('Frok Error')
                elif pid==0:
                    signal.signal(signal.SIGINT, signal.SIG_DFL)
                    try:
                        os.execvp(arg,line_arr)
                    except OSError:
                        print(f'{arg}: command not found')
                        os._exit(127)
                else:
                    c_pid,st=os.waitpid(pid,0)
                    signal.signal(signal.SIGINT, old_handler)
                    if os.WIFEXITED(st):
                        exit_code=os.WEXITSTATUS(st)
                    elif os.WIFSIGNALED(st):
                        signal_number=os.WTERMSIG(st)
                        print(f'terminated by signal: {signal_number}')
                        exit_code=signal_number+128
                        #print(f'CHILD PID:{c_pid} Exit:{exit_code}')
if __name__=='__main__':
    #print('MiniShell.PY ===')
    main()
