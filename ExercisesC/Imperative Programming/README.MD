<div class="description user_content enhanced" data-resource-type="assignment.body" data-resource-id="1746383"><p>Consider a simple OOP application, written in Java, which defines a PythogoreanTriple class and tests it with a driver.&nbsp; A Pythagorean Triple is a set of three numbers which could be the three sides of a possible right triangle.&nbsp; In this example, it is possible for two instances of my PythTriple class to be equivalent, but with side A and side B reversed, but this is not important for this purpose.</p>
<p>&nbsp;</p>
<p><strong>PythTriple.java:</strong></p>
<p>package pythex;</p>
<p>public class PythTriple {<br>&nbsp; &nbsp; private double sideA;<br>&nbsp; &nbsp; private double sideB;<br>&nbsp; &nbsp; private double hyp;</p>
<p>&nbsp; &nbsp; public void inputTwoSides(double sideAIn, double sideBIn) {<br>&nbsp; &nbsp; &nbsp; &nbsp; sideA = sideAIn;<br>&nbsp; &nbsp; &nbsp; &nbsp; sideB = sideBIn;<br>&nbsp; &nbsp; &nbsp; &nbsp; hyp = Math.sqrt(Math.pow(sideA, 2) + Math.pow(sideB, 2));<br>&nbsp; &nbsp; }</p>
<p>&nbsp; &nbsp; public void inputOneSideAndHyp(double sideAIn, double hypIn) {<br>&nbsp; &nbsp; &nbsp; &nbsp; sideA = sideAIn;<br>&nbsp; &nbsp; &nbsp; &nbsp; hyp = hypIn;<br>&nbsp; &nbsp; &nbsp; &nbsp; sideB = Math.sqrt(Math.pow(hyp, 2) - Math.pow(sideA, 2));<br>&nbsp; &nbsp; }</p>
<p>&nbsp; &nbsp; @Override<br>&nbsp; &nbsp; public String toString() {<br>&nbsp; &nbsp; &nbsp; &nbsp; return "PythTriple [sideA=" + String.format("%5.3f", sideA) + ", sideB=" + String.format("%5.3f", sideB)<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + ", hyp=" + String.format("%5.3f", hyp) + "]";<br>&nbsp; &nbsp; }</p>
<p>}</p>
<p>&nbsp;</p>
<p><strong>OOPPythDriver.java:</strong></p>
<p>&nbsp;</p>
<p>package pythex;</p>
<p>public class OOPPythDriver {<br>&nbsp; &nbsp; public static void main(String[] args) {<br>&nbsp; &nbsp; &nbsp; &nbsp; PythTriple[] pyths = new PythTriple[3];<br>&nbsp; &nbsp; &nbsp; &nbsp; PythTriple pt1 = new PythTriple();<br>&nbsp; &nbsp; &nbsp; &nbsp; pt1.inputOneSideAndHyp(3,5);<br>&nbsp; &nbsp; &nbsp; &nbsp; PythTriple pt2 = new PythTriple();<br>&nbsp; &nbsp; &nbsp; &nbsp; pt2.inputOneSideAndHyp(1, Math.sqrt(2));<br>&nbsp; &nbsp; &nbsp; &nbsp; PythTriple pt3 = new PythTriple();<br>&nbsp; &nbsp; &nbsp; &nbsp; pt3.inputTwoSides(2, 3);<br>&nbsp; &nbsp; &nbsp; &nbsp; pyths[0] = pt1;<br>&nbsp; &nbsp; &nbsp; &nbsp; pyths[1] = pt2;<br>&nbsp; &nbsp; &nbsp; &nbsp; pyths[2] = pt3;<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; for(PythTriple p: pyths)<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; System.out.println(p); &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; }&nbsp;<br>}</p>
<p>Run this code, either from a command line or with Eclipse or some other IDE. Then go over the code until you understand it.</p>
<p>Note that this small application relies heavily on OOP:</p>
<p>a) The data is represented using a Java class, with one instance of the class representing one Pythagorean triple.</p>
<p>b) The driver uses several of PythTriple's instance methods.</p>
<p>&nbsp;</p>
<p><span style="font-size: 24pt;"><strong>Assignment:</strong></span></p>
<p><br>Write a similar application in C, which requires you to do it <em>without using OOP.</em>&nbsp;</p>
<ul>
<li>Your entire application should be in one code file.</li>
<li>Represent the Pythagorean triples with a 3 x 3 array of doubles.</li>
<li>Write a function&nbsp; similar to the inputTwoSides method in the OOP version.&nbsp; This method should take values for side A, side B, and an array row index, calculate the hypotenuse, and add the values to the 2D array at the specified row.&nbsp; For example, if this method is called with parameters 3, 4, and 0, it will set triples[0][0] to 3, triples[0][1] to 4, and triples[0][2] to 5.</li>
<li>Write a function similar to the inputOneSideAndHyp method in the OOP version.</li>
<li>Write a main() method that uses the *same examples* used in my driver class and generates output formatted similarly to the output in the example.</li>
<li>The methods that do calculations should *not* produce any user output; the output must be done in main().</li>
<li>You may use global scope for the array (ie, declare the array at the top of the file, outside any functions.)&nbsp; Array declaration syntax is slightly different in C than in Java.&nbsp; The declaration will look like this:
<ul>
<li>double triples[3][3];</li>
</ul>
</li>
<li>The functions sqrt and pow are part of the math.h header file, so put this line of code right after the include for stdio.h:
<ul>
<li>#include &lt;math.h&gt;</li>
</ul>
</li>
<li>You can call these functions like this:
<ul>
<li>pow(base, exponent)&nbsp;&nbsp; for example, pow (2, 3) will return 8</li>
<li>sqrt(number) &nbsp;&nbsp; for example, sqrt(4) will return 2</li>
</ul>
</li>
<li>A list of printf formatting codes is available here: <a href="https://www.tutorialspoint.com/c_standard_library/c_function_printf.htm" target="_blank" class="external" rel="noreferrer noopener"><span>https://www.tutorialspoint.com/c_standard_library/c_function_printf.htm</span><span class="external_link_icon" style="margin-inline-start: 5px; display: inline-block; text-indent: initial; " role="presentation"><svg viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg" style="width: 1em; height: 1em; vertical-align: middle; fill: currentcolor; --noir-inline-fill: currentcolor;" data-noir-inline-fill="">
    <path d="M1226.667 267c88.213 0 160 71.787 160 160v426.667H1280v-160H106.667v800C106.667 1523 130.56 1547 160 1547h1066.667c29.44 0 53.333-24 53.333-53.333v-213.334h106.667v213.334c0 88.213-71.787 160-160 160H160c-88.213 0-160-71.787-160-160V427c0-88.213 71.787-160 160-160Zm357.706 442.293 320 320c20.8 20.8 20.8 54.614 0 75.414l-320 320-75.413-75.414 228.907-228.906H906.613V1013.72h831.254L1508.96 784.707l75.413-75.414Zm-357.706-335.626H160c-29.44 0-53.333 24-53.333 53.333v160H1280V427c0-29.333-23.893-53.333-53.333-53.333Z" fill-rule="evenodd"></path>
</svg>
<span class="screenreader-only">Links to an external site.</span></span></a>.&nbsp; Don't forget to prepend the % (for example, %d for base 10 integer)</li>
<li>You will need to add -lm to the command to compile the program with the math library. For example, if the program is called impex.c, the command to compile it to an executable named impex is
<ul>
<li>gcc -Wall -std=c17 -o impex impex.c -lm</li>
<li><strong>Use gcc. *Don't* use g++, the C++ compiler</strong></li>
</ul>
</li>
<li>
<p>After you write the code, consider this question: how would you do this if the different data variables were not all the same type, so that you could not use a 2D array?&nbsp; For example, if the data consisted of payroll records, each with a String for the employee's name, a long for an employee id, a double for the employee's hourly wage, and another double for the number of hours the employee worked this week?</p>
<p>&nbsp;</p>
</li>
</ul>
<p>Turn in your C code file and either a screenshot or copy-and-pasted output from the command line.&nbsp; Try to put the output in a single file.</p></div>