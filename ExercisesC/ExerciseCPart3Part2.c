#include <stdio.h>

int main(void)
{
	double GPA = 0.0; /* Initialization, required */
	int shoeSize = 0;
	char firstInitial='a';
	printf("What is your GPA, show size, and first initial?: \n");
	scanf("%lf, %d, %c", &GPA, &shoeSize, &firstInitial);
	printf("GPA is %f, shoe size is %d, first initial is %c \n", GPA, shoeSize, firstInitial);
}
