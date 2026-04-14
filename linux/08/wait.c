#include <unistd.h>
#include <stdio.h>
int main(int argc, char** argv) {
        if(argc<2) { puts("argc < 2. error"); return 1;}
        int num = atoi(argv[1]);
        printf("sleep : %d\n",num);
        sleep(num);
        printf("end sleep ");
        return 0;
}
