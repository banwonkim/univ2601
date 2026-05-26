# ls wc 아무든 셸 프로세스가 만든다는데 잘 모르겠고 


import os
r,w=os.pipe()
pid=os.fork()

# child
if pid==0:
    # 왜 닫음?
    os.close(r)
    # w에 msg 전달?
    msg = f'PID {os.getpid()}'.encode()
    os.write(w, msg)
    os.close(w)
    os._exit(0)
else:
    # w는 또 왜 닫고.
    os.close(w)
    # r에서 1024 바이트 읽는건데 뭘 어떻게 한다는겨
    data=os.read(r,1024)
    # r 닫는건 쓸모없으니까 그런거라고 대충 보고
    os.close(r)
    # 자식 프로세스 끝날때까지 기다리고
    os.waitpid(pid, 0)
    # 받은 메세지 출력일듯
    print(f'[{os.getpid()}] {data.decode()}', end='')
