#include <stdio.h>
#include <math.h>

double triples[3][3];



double inputTwoSides(double sideAIn, double sideBIn, int rowIndex)
{
	double hyp = sqrt(pow(sideAIn, 2) + pow(sideBIn, 2));
	triples[rowIndex][0]=sideAIn;
	triples[rowIndex][1]=sideBIn;
	triples[rowIndex][2]=hyp;
	return hyp;
}
double inputOneSideAndHyp(double sideAIn, double hypIn, int rowIndex)
{
	double sideB = sqrt(pow(hypIn, 2) - pow(sideAIn, 2));
	triples[rowIndex][0]=sideAIn;
	triples[rowIndex][1]=sideB;
	triples[rowIndex][2]=hypIn;
	return sideB;
}

int main(void)
{
	printf("With a side of length %lf and hypotenuse of length %lf, the missing side is %lf \n", 3.0, 5.0, inputOneSideAndHyp(3,5,0));
	printf("With a side of length %lf and hypotenuse of length %lf, the missing side is %lf \n", 1.0, sqrt(2), inputOneSideAndHyp(1, sqrt(2), 1));
	printf("With a side of length %lf and side of length %lf, the hypotenuse is %lf \n", 2.0, 3.0, inputOneSideAndHyp(3,5,2));
	for(int i=0; i<3; i++) {
		for(int j=0; j<3; j++) {
			printf("[%d][%d] has a value of %lf \n", i,j,triples[i][j]);
		}
	}
	return 0;
}
