# README.md
1. How To Run : python3 miniconda.py
2. exit, status, help
3. fg jobs cd bg
4.
- 정상 명령 실행
```$ python3 minishell.py
mini$ echo hello
hello
mini$ pwd
/home/user
mini$ status
last exit code: 0
mini$ exit
```
- 종료 코드 확인
```
$ python3 minishell.py
mini$ true
mini$ status
last exit code: 0
mini$ false
mini$ status
last exit code: 1
mini$ exit 0
```
- 존재하지 않는 명령 실행
```
$ python3 minishell.py
mini$ no_such_command
no_such_command: command not found
mini$ status
last exit code: 127
mini$ exit
```
5. 자식 프로세스의 경우 pid==0, 부모 프로세스 에서는 pid가 0 초과의 양수가 됨. 자식에서는 os.execvp를 통해 외부 프로세스를 호출, 명령어가 없어서 실패할 경우 종료코드 127을 반환 후 종료. 부모 프로세스는 os.waitpid를 통해 자식 프로세스가 종료될 때 까지 대기한다. 자식 프로세스가 종료될 경우 종료코드를 확인하고, exit_code(최근의 종료 코드)에 해당 값을 저장한다. 만일 시그널로 종료된 경우에는 terminated by signal: 메세지를 출력하고, signal_number에 128을 더해서 exit_code를 갱신한다.
6. 자식 프로세스에서 os._exit(0)를 호출해서 자식 프로세스는 종료되고, 부모 프로세스의 부분으로 돌아옴 (os.waitpid)
7. 자식 프로세스가 종료되기 이전에 부모 프로세스가 작동될때 별도로 동작하므로 실행 순서가 맞지 않아 오류 발생.
