<p><strong>Write a C application that creates an array of three instances of a struct that represents a car.&nbsp; Calculate and print the average miles per gallon of the cars.</strong></p>
<ol>
<li><span> (20 points) Write a header file that a) defines a struct called car, which has a double for the weight of the car and a double for its gas mileage (miles per gallon) and b) declares a prototype for a function called get_avg_mpg, which takes a pointer to a car and an int for the length of an array, and returns a double.</span></li>
</ol>
<ol start="2">
<li><span> Write C code that does the following:&nbsp;</span>
<ol style="list-style-type: upper-alpha;">
<li><span> (30 points) defines the function get_avg_mpg that was declared in the header file.&nbsp; The function should use </span><strong>pointer arithmetic</strong><span> to iterate through the array of cars and calculate and return the average (mean) mpg.&nbsp; Don't print anything in this function.&nbsp;</span></li>
<li><span> (50 points) has a main() that creates an array of three cars </span><strong>on the heap using malloc() </strong><span>and uses </span><strong>pointer arithmetic</strong><span> to iterate through the array and set values for the weight and mpg of each car, then calls get_avg_mpg and prints the result using printf (use the formatting code %.2f).&nbsp; You do not need to take user input; the values for the cars can be hard-coded.</span></li>
</ol>
</li>
</ol>
