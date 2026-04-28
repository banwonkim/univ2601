import os
def main():
    pid=os.fork()
    if pid==0:
        print("Child : ",os.getpid())
        for i in range(0,10): print(i, end=' ')
        print()
    else:
        print("Parent : ", os.getpid())
        for i in range(10,20): print(i, end=' ')
        print()

if __name__=='__main__':
	main()
