#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char ** argv)
{
	if(argc!=3){
		printf("%s\n", "wrong input arguments number");
		exit(-1);
	}
	char* from = argv[1];
	char* to = argv[2];

	if(strlen(from)!=strlen(to)){
		printf("%s\n", "from and to are with different length");
		exit(-1);
	}
	int len = strlen(from);
	for (int i=0; i<len; i++){
		for (int j=i+1; j<len; j++){
			if(from[i]==from[j]){
				printf("%s\n", "there are duplicates in from input");
				exit(-1);
			}
		}
	}

	char letter[1];
lable1:	while ((read(0, letter, 1))>0){
		for(int i=0; i<len; i++){
			if(letter[0]==from[i]){
				write(1, &to[i], 1);
				goto lable1;
			}
			}
		write(1, &letter, 1);
		}
	printf("\n");
	return 0;
}
