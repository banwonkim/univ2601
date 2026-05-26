#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
void alarmHandle(int signo){
	printf("SHut up\n");
	sleep(2);
	printf("Shut up2\n");
}
int main(){
	signal(SIGALRM, alarmHandle);
	alarm(5);
	for (int i=0;i<10;i++){
		sleep(1);
		printf("%d sec\n", i);
	}
	return 0;
}
