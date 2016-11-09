#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

	int letter;
lable1:	while ((letter=getchar())!=EOF){
		for(int i=0; i<len; i++){
			if(letter==from[i]){
				putchar(to[i]);
				goto lable1;
			}
			}
		putchar(letter);
			
	}
	printf("\n");
	return 0;
}
