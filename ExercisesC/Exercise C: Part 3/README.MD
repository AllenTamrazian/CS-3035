<div class="show-content user_content clearfix enhanced" data-resource-type="wiki_page.body" data-resource-id="1792505" data-lti-page-content="true">
  
    <h1 class="page-title">Ungraded Exercises: C, Part III<button aria-haspopup="dialog" class="ally-accessible-versions ally-add-tooltip" data-id="page:1792505" data-ally-content-id="page:1792505" data-ally-richcontent-eid="page:1792505" aria-label="Alternative formats" title="Alternative formats">
    <span class="ally-prominent-af-download-button"></span>
</button></h1>
  
  
  
    <p>1a) write a program in C that uses scanf to take input for two doubles and uses printf to print the result.&nbsp; Here is output from my solution:<br>3.141590 + 7.432100 = 10.573690</p>
<p>Note: use the format code lf for doubles</p>
<p>1b) modify the program from 1a so that it prints the result of the addition to 3 digits past the decimal point.&nbsp; Use the code %.3lf</p>
<p>&nbsp;</p>
<p>2) Do 1a and 1b again, but use a separate function to do the addition.&nbsp; The function should take pointers to the two doubles, but return a double rather than a pointer.&nbsp; Then try it with the function returning a pointer.&nbsp; If you try this a few times, it is likely to crash, at least sometimes, with a segmentation fault error.&nbsp; See if you can understand what is going on.</p>
<p>&nbsp;</p>
<p>3) Write a program in C that asks the user for a student's GPA (double), shoe size(int), and first initial (char), separated by commas in one line of input, assigns those values to variables, and prints them out separately.&nbsp; Here is output from my solution:</p>
<p>Please enter a student's GPA, shoe size, and first initial, separated by commas: 3.27,11,X<br>The student's GPA is 3.270, shoe size is 11, and first initial is X</p>
<p>Use the format code %c for the char.<br>Hint: to see how to handle the commas, see the lecture example in which I separate the digits of pi before and after the decimal point</p>
<p>&nbsp;</p>
<p>4) Write a program in C that:</p>
<p>creates an array of doubles that represents the GPAs of four students</p>
<p>uses <em><strong>pointer arithmetic</strong>, </em>printf, and scanf to take input for the four students' GPAs (see the lecture notes for several different ways you could set up the loop).&nbsp; Note that the pointer in the loop is already an address, so the variable used to tell scanf where to put the data it reads in does not need an extra &amp; (for example, if the pointer is called next, put the data at next, rather than &amp;next.)</p>
<p>uses <em><strong>pointer arithmetic</strong> </em>and<em> </em>printf to show the values from the array.&nbsp; Note that you need to print the data the pointer points to, not the pointer itself, so you will need the dereferencing *.&nbsp; For example, if the pointer is called next, you specify what to print with *next, that is, "the data next points to".</p>
  
<div id="assign-to-mount-point"></div>
</div>