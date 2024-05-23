#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct triangle
{
	double sideAIn;
	double sideBIn;
	double hypIn;
};

double inputTwoSides(struct triangle *t)
{
	double hyp = sqrt(pow(t->sideAIn, 2) + pow(t->sideBIn, 2));
	t->hypIn=hyp;
	return hyp;
}

double inputOneSideAndHyp(struct triangle *t)
{
	double sideB = sqrt(pow(t->hypIn, 2) - pow(t->sideAIn, 2));
	t->sideBIn=sideB;
	return sideB;
}

int main(void)
{
	struct triangle *triangles = (struct triangle *)malloc(3 * sizeof(struct triangle));
	
	triangles[0].sideAIn=3.0;
	triangles[0].hypIn=5.0;
	printf("With a side of length %lf and hypotenuse of length %lf, the missing side is %lf \n", 3.0, 5.0, inputOneSideAndHyp(&triangles[0]));
	
	triangles[1].sideAIn=1.0;
	triangles[1].hypIn=sqrt(2);
	printf("With a side of length %lf and hypotenuse of length %lf, the missing side is %lf \n", 1.0, sqrt(2), inputOneSideAndHyp(&triangles[1]));
	
	
	triangles[2].sideAIn=2.0;
	triangles[2].sideBIn=3.0;
	printf("With a side of length %lf and side of length %lf, the hypotenuse is %lf \n", 2.0, 3.0, inputTwoSides(&triangles[2]));
	
	for(int i=0; i<3; i++) {
			printf("Triangle %d values: %lf, %lf, %lf \n", i, triangles[i].sideAIn, triangles[i].sideBIn, triangles[i].hypIn);
	}
	
	free(triangles);
	
	return 0;
}

