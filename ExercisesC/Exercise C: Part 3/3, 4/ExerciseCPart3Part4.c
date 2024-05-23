#include <stdio.h>

int main(void)
{
	double GPAList[4];
	
	for(int counter = 0; counter < 4; counter++){ 
		printf("Tell me the GPA of student %d ", counter+1);
		scanf("%lf", &GPAList[counter]);
	}
	double *begin=GPAList;
	double *last = begin+4;
	for(; begin<last; begin++){ 
		printf("GPA of all students in order is %lf \n", *begin);
	}
}
