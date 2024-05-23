#include "Checkpoint1.h"

double get_avg_mpg(struct car *cars, int length)
{
	double sum;
	double average;
	struct car *v, *last;
	last=cars[length-1];
	for(v=cars; v<=last; v++)
	{
		sum=sum+(v)->gasMileage;
	}
	average=sum/length;
	return average;
}
