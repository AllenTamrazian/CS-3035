<div class="description user_content enhanced" data-resource-type="assignment.body" data-resource-id="1749521"><p><strong>Write a multithreaded Python OOP application that models a pancake restaurant with multiple cooks and multiple customers, each of which runs in its own thread. </strong></p>
<p>Notes:</p>
<ul>
<li>For this assignment, you will need to generate pseudorandom numbers.&nbsp; Use this import: <em>from random import random,</em> and call the method random(), which generates a pseudorandom floating point value between 0 and 1.&nbsp; Multiply it by the maximum value you want. For example, the generate a pseudorandom number between 0 and 3, call random() and multiply the result by 3.</li>
<li>The entire application contains only *one* stack of pancakes.&nbsp; All cooks add to , and all customers eat from, the same stack.</li>
</ul>
<p>&nbsp;</p>
<p>Part I (5 points): Write the class Pancake.&nbsp; Pancake needs a class variable that will always show the number of Pancakes that have been created (initially 0) and&nbsp; reasonable __str__ and __init__ methods.</p>
<p>Part II (20 points): Write the Cook class.&nbsp; Cook needs a name and a reference to a stack of pancakes (although, of course, nothing in the Cook code will show that it is a stack or what kind of object may be in the stack). Cook also needs these methods:</p>
<ul>
<li>cook_pancake creates a pancake, prints a message like "Cathy the cook cooks pancake # 12", and returns a reference to the pancake</li>
<li>work contains an infinite loop which uses cook_pancake to get a pancake, puts it on the stack, and then sleeps for a random amount of time (for example, up to two seconds).&nbsp; The sleep time represents the amount of time it takes a Cook to cook a pancake.</li>
<li>reasonable __str__ and __init__ methods&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
</ul>
<p>Part III (20 points): Write the Customer class.&nbsp; Customer needs a name and a reference to a stack of pancakes.&nbsp; Besides resonable __init__ and __str__ methods, it also needs these methods:</p>
<p>eat_pancake takes a reference to a pancake and prints a message like "Carlos the customer eats pancake #27"</p>
<p>dine contains an infinite loop.&nbsp; If there are no pancakes on the stack, it prints a message similar to this: "No pancakes ready to eat!" If there is at least one pancake on the stack, it removes the top pancake and sends it as the argument to eat_pancake.&nbsp; Either way, code inside the loop calls sleep() to sleep for some random amount of time.&nbsp; This time represents the amount of time it takes a customer to eat a pancake.</p>
<p>Part IV (45 points): Write the PancakeHouse class.&nbsp; PancakeHouse needs a stack (use the synchronized class LifoQueue from the same queue package used for a regular queue in the lecture notes), a list of cooks, and a list of customers.&nbsp; PancakeHouse also needs these methods:</p>
<ul>
<li>reasonable __str__ and __init__ methods</li>
<li>add_cook and add_customer each takes a name, creates a Cook or Customer with that name (you will also need to send a reference to the stack), and adds the cook or customer to the appropriate list.</li>
<li>begin_shifts creates and starts a thread for each Cook (using the Cook's work() method as the target)</li>
<li>serve_customers creates and starts a thread for each customer (using the Customer's dine() method as the target)</li>
<li>open takes an argument for the number of seconds the PancakeHouse will be open.&nbsp; It calls begin_shifts and serve_customers, then runs for the specified amount of time.&nbsp; Use sleep(1) in a loop, to cut down on CPU usage form checking the time excessively frequently.&nbsp; At the end of the time, print the number of uneaten pancakes, and then print the __str__ fo each pancake remaining in the stack.&nbsp; Then exit the program.<br>&nbsp;</li>
</ul>
<p>Part V (10 points): write driver code that does the following: &nbsp;</p>
<p>creates a PancakeHouse</p>
<p>adds at least two cooks with different names&nbsp;</p>
<p>adds at least two customers with different names</p>
<p>calls open() on the PancakeHouse, sending some reasonable value (say, 60) for the amount of time the Pancake House will be open.</p>
<p>&nbsp;</p>
<p>Here is some of the output from my solution:<br>Cathy cooks Pancake # 1<br>Carlos cooks Pancake # 2<br>Camillo eats Pancake # 2<br>Carrie eats Pancake # 1<br>No pancakes ready to eat!<br>0 uneaten pancakes<br>Carlos cooks Pancake # 3<br>Camillo eats Pancake # 3<br>Cathy cooks Pancake # 4<br>1 uneaten pancakes<br>Carlos cooks Pancake # 5<br>Cathal eats Pancake # 5<br>Carlos cooks Pancake # 6<br>Cathal eats Pancake # 6<br>Carrie eats Pancake # 4<br>No pancakes ready to eat!</p>
<p>[many lines of output omitted]</p>
<p>6 uneaten pancakes<br>Camillo eats Pancake # 58<br>Cathal eats Pancake # 57<br>Carlos cooks Pancake # 59<br>Cathy cooks Pancake # 60<br>Cathy cooks Pancake # 61<br>Carrie eats Pancake # 61<br>6 uneaten pancakes<br>Pancake # 60<br>Pancake # 59<br>Pancake # 45<br>Pancake # 24<br>Pancake # 22<br>Pancake # 21</p>
<p>&nbsp;</p>
<p>Submit all your code in one file, as well as a cut and paste or screenshot of the output from running your driver.<br>&nbsp; &nbsp;</p></div>
