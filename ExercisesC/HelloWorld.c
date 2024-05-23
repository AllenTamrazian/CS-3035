#include <stdio.h>


int distanceConversion(int number1, int number2)
{
	int biggerNumber;
	int smallerNumber;
	if(number1>number2)
	{
		biggerNumber = number1;
		smallerNumber = number2;
	} 
	else {
		biggerNumber = number2;
		smallerNumber = number1;
	}
	
	float kilometer=(smallerNumber-1)*1.609;
	for(int i=smallerNumber-1; i<biggerNumber; i++)
	{
		kilometer=kilometer+1.609;
		smallerNumber=smallerNumber+1;
		printf("%d mile = %f KM \n", smallerNumber-1, kilometer);
	}
	
	return 0;
}

int main(void)
{
	distanceConversion(10, 1);
	distanceConversion(2, 15);
	return 0;
}
