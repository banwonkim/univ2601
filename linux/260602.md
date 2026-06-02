# 13장 소켓
배고파

## 클라
```py
import socket
import time
print('Here Client')
cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(('localhost', 8080))
time.sleep(1)
while True:
    com=input('Enter command $' )
    cli.sendall(com.encode())
    res=data=cli.recv(4096).decode()
    print('command output :', res)
cli.close()
```

## 서버
```py
import socket
import os

def handle_client(cli):
    try:
        com=cli.recv(1024).decode()
        if not com:
            return
        pid=os.fork()
        if pid==0: # cild proc
            os.dup2(cli.fileno(), 1)
            os.dup2(cli.fileno(), 2)
            os.execlp(com.split()[0],
                      *com.split())
        else:
            os.waitpid(pid, 0)

    except Exception as e:
        cli.sendall(f'Error {str(e)}'.encode())
    finally:
        cli.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 8080))
serv.listen(5)
print('Serv Run port 8080')

while True:
    cli, addr = serv.accept()
    print('Conn addr : ', addr)
    handle_client(cli)

```
## 출력 결과 근데 실패함
``` 
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
Conn addr :  ('127.0.0.1', 38458)
```

뭔가 실패함
