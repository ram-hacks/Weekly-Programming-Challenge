#include <stdio.h>
#include <stdlib.h>

void check(char[][9], int);
void exit();

int main() { 

char arr[8][9];

for(int i = 0; i < 8; i++)
	scanf("%s", *(arr+i));

for(int i = 0; i < 8; i++)
	check(arr, i);

int count = 0;
for(int i = 0; i < 8; i++)
	for(int j = 0; j < 8; j++)
		if (arr[i][j] == '*')
			count++;
if(count != 8)
	exit();

printf("valid");
}

void exit() {
	printf("invalid");
	exit(0);
}


void check(char arr[][9], int col) {

	int c = 0;
	int r = 0;
	//check col/row
	for(int i = 0; i < 8; i++){
		if(arr[i][col] == '*') {
			c++;
			for(int j = 0; j < 8; j++)
				if (arr[i][j] == '*')
					r++;

			if (r > 1)
				exit();
			r = 0;
		}
	}
	if (c > 1)
		exit();	
//	printf("Passed row/cols\n");
	//check diag
	
	for(int i = 0; i < 8; i++){
		if(arr[i][col] == '*') {
			int k = i-1;
			int j = col-1;
			while(k >= 0 && j >= 0) {
				if(arr[k][j] == '*')
					exit();
				k--;
				j--;
			}
			//printf("Passed upper\n");
			
			k = i+1;
			j = col-1;
			while(k < 8 && j >= 0) {
				if(arr[k][j] == '*')
					exit();
				k++;
				j--;
			}
			//printf("Passed lower\n");
		}
	}
	
	

}
