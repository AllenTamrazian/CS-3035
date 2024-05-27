<p>3) Write a program in C that asks the user for a student's GPA (double), shoe size(int), and first initial (char), separated by commas in one line of input, assigns those values to variables, and prints them out separately.&nbsp; Here is output from my solution:</p>
<p>Please enter a student's GPA, shoe size, and first initial, separated by commas: 3.27,11,X<br>The student's GPA is 3.270, shoe size is 11, and first initial is X</p>
<p>Use the format code %c for the char.<br>Hint: to see how to handle the commas, see the lecture example in which I separate the digits of pi before and after the decimal point</p>
<p>&nbsp;</p>
<p>4) Write a program in C that:</p>
<p>creates an array of doubles that represents the GPAs of four students</p>
<p>uses <em><strong>pointer arithmetic</strong>, </em>printf, and scanf to take input for the four students' GPAs (see the lecture notes for several different ways you could set up the loop).&nbsp; Note that the pointer in the loop is already an address, so the variable used to tell scanf where to put the data it reads in does not need an extra &amp; (for example, if the pointer is called next, put the data at next, rather than &amp;next.)</p>
<p>uses <em><strong>pointer arithmetic</strong> </em>and<em> </em>printf to show the values from the array.&nbsp; Note that you need to print the data the pointer points to, not the pointer itself, so you will need the dereferencing *.&nbsp; For example, if the pointer is called next, you specify what to print with *next, that is, "the data next points to".</p>
  
<div id="assign-to-mount-point"></div>
