#include <stdio.h>

int bunnyEars(int n) {
    if(n < 0) return -1;
    if(n == 0) return 0;
    return 2 + bunnyEars(n - 1);
}

int factorial(int n) {
    if(n < 0) return -1;
    if(n == 0) return 1;
    return n * factorial(n - 1);
}

int fib(int n) {
    if(n < 0) return -1;
    if(n == 0) return 0;
    if(n == 1) return 1;
    return fib(n-1) + fib(n - 2);
}


int power(int base, int exp) {
    if(exp < 0) return -1;
    if(exp==0) return 1;
    return (base * power(base, exp - 1));
}


int main(void)
{
	printf("Number of ears for %d bunnies : %d \n",2, bunnyEars(2));
	printf("Factorial of %d is %d \n",4, factorial(4));
	printf("Fibonacci number for %d is %d \n",4, fib(4));
	printf("%d to the power of %d is %d \n",2,2,power(2, 2));
	return 0;
}
