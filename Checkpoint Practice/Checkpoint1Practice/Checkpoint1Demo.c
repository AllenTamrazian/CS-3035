#include <stdio.h>
#include <stdlib.h>
#include "Checkpoint1.h"


int main(void)
{
	struct car *carList = (struct car *) malloc(3 * sizeof(struct car));
	carList[0].weight=2500;
	carList[0].gasMileage=30;
	carList[1].weight=6000;
	carList[1].gasMileage=10;
	carList[2].weight=3500;
	carList[2].gasMileage=25;
	printf("%f \n",get_avg_mpg(carList, 3));
	return 0;
}


