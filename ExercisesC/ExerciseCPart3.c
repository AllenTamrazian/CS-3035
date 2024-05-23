#include <stdio.h>

double addition(double *firstDouble, double *secondDouble)
{
	return *firstDouble+*secondDouble;
}

int main(void){
	double firstDouble=0;
	double secondDouble=0;
	printf("Type in a double \n");
	scanf("%lf", &firstDouble);
	printf("Type in another double \n");
	scanf("%lf", &secondDouble);
	printf("%lf + %lf =%.3lf \n", firstDouble, secondDouble, addition(&firstDouble, &secondDouble));
	return 0;
}
