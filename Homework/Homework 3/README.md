Write a multithreaded Python OOP application that models a pancake restaurant with multiple cooks and multiple customers, each of which runs in its own thread.

Notes:

For this assignment, you will need to generate pseudorandom numbers.  Use this import: from random import random, and call the method random(), which generates a pseudorandom floating point value between 0 and 1.  Multiply it by the maximum value you want. For example, the generate a pseudorandom number between 0 and 3, call random() and multiply the result by 3.
The entire application contains only *one* stack of pancakes.  All cooks add to , and all customers eat from, the same stack.
 

Part I (5 points): Write the class Pancake.  Pancake needs a class variable that will always show the number of Pancakes that have been created (initially 0) and  reasonable __str__ and __init__ methods.

Part II (20 points): Write the Cook class.  Cook needs a name and a reference to a stack of pancakes (although, of course, nothing in the Cook code will show that it is a stack or what kind of object may be in the stack). Cook also needs these methods:

cook_pancake creates a pancake, prints a message like "Cathy the cook cooks pancake # 12", and returns a reference to the pancake
work contains an infinite loop which uses cook_pancake to get a pancake, puts it on the stack, and then sleeps for a random amount of time (for example, up to two seconds).  The sleep time represents the amount of time it takes a Cook to cook a pancake.
reasonable __str__ and __init__ methods        
Part III (20 points): Write the Customer class.  Customer needs a name and a reference to a stack of pancakes.  Besides resonable __init__ and __str__ methods, it also needs these methods:

eat_pancake takes a reference to a pancake and prints a message like "Carlos the customer eats pancake #27"

dine contains an infinite loop.  If there are no pancakes on the stack, it prints a message similar to this: "No pancakes ready to eat!" If there is at least one pancake on the stack, it removes the top pancake and sends it as the argument to eat_pancake.  Either way, code inside the loop calls sleep() to sleep for some random amount of time.  This time represents the amount of time it takes a customer to eat a pancake.

Part IV (45 points): Write the PancakeHouse class.  PancakeHouse needs a stack (use the synchronized class LifoQueue from the same queue package used for a regular queue in the lecture notes), a list of cooks, and a list of customers.  PancakeHouse also needs these methods:

reasonable __str__ and __init__ methods
add_cook and add_customer each takes a name, creates a Cook or Customer with that name (you will also need to send a reference to the stack), and adds the cook or customer to the appropriate list.
begin_shifts creates and starts a thread for each Cook (using the Cook's work() method as the target)
serve_customers creates and starts a thread for each customer (using the Customer's dine() method as the target)
open takes an argument for the number of seconds the PancakeHouse will be open.  It calls begin_shifts and serve_customers, then runs for the specified amount of time.  Use sleep(1) in a loop, to cut down on CPU usage form checking the time excessively frequently.  At the end of the time, print the number of uneaten pancakes, and then print the __str__ fo each pancake remaining in the stack.  Then exit the program.
 
Part V (10 points): write driver code that does the following:  

creates a PancakeHouse

adds at least two cooks with different names 

adds at least two customers with different names

calls open() on the PancakeHouse, sending some reasonable value (say, 60) for the amount of time the Pancake House will be open.

 

Here is some of the output from my solution:
Cathy cooks Pancake # 1
Carlos cooks Pancake # 2
Camillo eats Pancake # 2
Carrie eats Pancake # 1
No pancakes ready to eat!
0 uneaten pancakes
Carlos cooks Pancake # 3
Camillo eats Pancake # 3
Cathy cooks Pancake # 4
1 uneaten pancakes
Carlos cooks Pancake # 5
Cathal eats Pancake # 5
Carlos cooks Pancake # 6
Cathal eats Pancake # 6
Carrie eats Pancake # 4
No pancakes ready to eat!

[many lines of output omitted]

6 uneaten pancakes
Camillo eats Pancake # 58
Cathal eats Pancake # 57
Carlos cooks Pancake # 59
Cathy cooks Pancake # 60
Cathy cooks Pancake # 61
Carrie eats Pancake # 61
6 uneaten pancakes
Pancake # 60
Pancake # 59
Pancake # 45
Pancake # 24
Pancake # 22
Pancake # 21

 

Submit all your code in one file, as well as a cut and paste or screenshot of the output from running your driver.
