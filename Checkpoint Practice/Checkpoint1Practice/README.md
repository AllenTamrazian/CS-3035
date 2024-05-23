<ol>
  <li>(20 points) Write a header file that a) defines a struct called car, which has a double for the weight of the car and a double for its gas mileage (miles per gallon) and b) declares a prototype for a function called get_avg_mpg, which takes a pointer to a car and an int for the length of an array, and returns a double.</li>
  <li>Write C code that does the following: 
    <ol> 
      <li type="A">(30 points) defines the function get_avg_mpg that was declared in the header file.  The function should use pointer arithmetic to iterate through the array of cars and calculate and return the average (mean) mpg.  Don't print anything in this function. </li>
      <li type="A">(50 points) has a main() that creates an array of three cars on the heap using malloc() and uses pointer arithmetic to iterate through the array and set values for the weight and mpg of each car, then calls get_avg_mpg and prints the result using printf (use the formatting code %.2f).  You do not need to take user input; the values for the cars can be hard-coded.</li>
    </ol>
  </li>
</ol>
