<div class="description user_content enhanced" data-resource-type="assignment.body" data-resource-id="1746373"><p>Write <strong>recursive</strong> C functions to do the following:</p>
<p><strong>Example:</strong></p>
<p>int summ(int n) returns the summation of integers from 0 to n.&nbsp; Here is the code.</p>
<p>int summ(int n) {<br>&nbsp; &nbsp; if(n &lt; 0) return -1;<br>&nbsp; &nbsp; if(n == 0) return 0;<br>&nbsp; &nbsp; return n + summ(n - 1);<br>}</p>
<p>1 (22 points) int bunnyEars(int n) returns -1 if n is less than 0, otherwise returns 2 + the number of ears for n-1 bunnies.</p>
<p>2. (23 points) int factorial(int n) returns -1 if n is less than 0, 1 if n == 0, otherwise n * the factorial of n - 1<br>3. (22 points) int fib(int n) returns -1 if n is less than 0, returns 0 if n is 0, returns 1 if n is 1, otherwise returns fib of n - 1 plus fib of n - 2.&nbsp; (If you test this with numbers greater than about 50, it will be very slow.)</p>
<p>4. (23 points) int posPow(int base, int exp) returns -1 if exp is less than 0, otherwise recursively calculates and returns base raised to the power exp.</p>
<p>5. (optional) int numDigits(int n) returns the number of digits in n. Hint: in C, as in Java, int division returns an int; any digits that would be after the decimal point are lost, so that, for example, 5/4 is 1.</p>
<p>6. (10 points) Write a main() that tests all the other functions thoroughly.</p>
<p>Turn in your code and a .txt file with a copy and paste of the output from running your program.</p>
<p>&nbsp;</p></div>