<h1 class="page-title">Sample Exam Part II: Code on Paper</h1>
  
  
  
<p>On the actual exam, this part will be closed-book, closed-notes, code-on-paper.&nbsp; For the practice exam, you may want to write the code on paper for the best practice.</p>
<p>&nbsp;</p>
<p><strong>Python </strong>programming problem, 25 points</p>
<p>Write a Cryptid Abstract Base Class and implement it with a Yeti class.&nbsp;</p>
<p>A Cryptid has a name and a height.&nbsp; The Cryptid ABC needs an&nbsp; __init__ that takes arguments and sets these instance variables. It also needs an abstract attack method that takes the location of the attack as an argument and a method that overloads the == operator. This will involve comparing the names and heights of the two Cryptids.&nbsp; For the height comparison, use isClose().</p>
<p>Yeti is a subclass of Cryptid.&nbsp; It's __init__ should pass the variables up to Cryptid's __init__. It needs a __str__ that returns a String like "Yann the Yeti is 3.2 meters tall" It should implement the attack(location) method by printing a String like</p>
<p>"Yann the Yeti throws ice at the citizens of Beijing"</p>
<p>using the actual name of the Yeti and the actual attack location</p>
<p>Yeti also needs a method that overloads the + operator to return a <strong>new Yeti</strong> with the combined names of the original ones (eg, "YannYolanda") and their combined heights.</p>
<p>&nbsp;</p>
<p>Use this import:</p>
<p>from abc import ABC, abstractmethod</p>
<p>&nbsp;</p>
<p><strong>Kotlin</strong><span> programming problem 1, 15 points:</span></p>
<p><span>Write a tail-recursive function that takes a positive Int n and uses a tail recursive helper function to calculate and return 2 ^ n (that is, two to the power n).&nbsp; Don't use Math.pow; think about how the recursive calculation will work.</span></p>
<p>&nbsp;</p>
<p><strong>Kotlin</strong><span> programming problem 2, 10 points:</span></p>
<p><span>Write a higher-order function with an expression body that takes an Int n and a function f from Int to Int and returns the result of calling f(f(n)).&nbsp; For example, if you call the function with n = -5 and a function that calculates absolute value, your function will return 5, and if you send the value 2 and a function that calculates the square of an Int, the function will return 16. In addition to the function, write the syntax to call it with a) with a function name as the function argument and b) with some lambda expression as the function argument.&nbsp;</span></p>
  
<div id="assign-to-mount-point"></div>
</div>
