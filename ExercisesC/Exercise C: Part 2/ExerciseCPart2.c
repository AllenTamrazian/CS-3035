#include <stdio.h>

void input(int my_array[], int length)
{
	for(int i=0; i<(sizeof(*my_array)-1); i++)
	{
		my_array[i] = 42;
	}
}

void countWhile(void)
{
	int i=0;
	while(i<100)
	{
		printf("%d \n", i);
		i++;
	}
}
void countDo(void)
{
	int i=0;
	do {
		printf("%d \n", i);
		i++;
	}
	while(i<100);
}

void countSwitch(int i)
{
	switch (i) {
        case 1:
            printf("Case 1 is Matched.");
            break;
 
        case 2:
            printf("Case 2 is Matched.");
            break;
 
        case 3:
            printf("Case 3 is Matched.");
            break;
 
        default:
            printf("Default case is Matched.");
            break;
    }
}

int main(void)
{
	int my_array[5];
	printf("array: %p \n", my_array);
	for(int i=0; i<(sizeof(my_array))-1; i++)
	{
		printf("before: %d \n", my_array[i]);
	}
	input(my_array, (sizeof(*my_array)-1));
	for(int i=0; i<(sizeof(my_array)-1); i++)
	{
		printf("after: %d \n", my_array[i]);
	}
	countWhile();
	countDo();
	countSwitch(1);
	return 0;
}
