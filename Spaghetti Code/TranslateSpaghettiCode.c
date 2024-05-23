#include <stdio.h>

void circumference(int radius, double constant)
{
	double circumference=radius*2*constant;
	printf("Circumference of radius %d is %f \n", radius, circumference);
}

int main(void)
{
	double const PI = 3.14;
	int r=4;
	circumference(r,PI);
	r=8;
	circumference(r,PI);
	return 0;
}
