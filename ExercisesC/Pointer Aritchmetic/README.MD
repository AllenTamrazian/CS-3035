<h1 class="page-title">Ungraded Exercise: Pointer Arithmetic</h1>
<p>1) Compile, run, and study this C program:</p>
<pre><code><span>#include &lt;stdio.h&gt;</span></code><br><br>int main(void){<br><br>// note the array declaration format is slightly different from Java<br>&nbsp;&nbsp; int myInts[] = {0, 1, 2, 3, 4}; <br>// declare an int pointer called pi and set it to point to the beginning of the array<br>// note that an array variable is a pointer to the beginning of the array<br>&nbsp;&nbsp;&nbsp; int *pi = myInts;<br>&nbsp;&nbsp;&nbsp; for(int counter = 0; counter &lt; 5; counter++){<br>/* printf is also available in Java, but you may never have used it.<br>printf uses formatting codes like %p for pointer (addresses expressed in bytes in hexadecimal) <br>and %d for (decimal) int <br>*/<br>&nbsp; &nbsp; &nbsp; <span>printf("Address %p: Value %d\n", pi, *pi);</span><br>// incrementing a pointer changes it by the size of the type to which it points<br>&nbsp;&nbsp; &nbsp; &nbsp; pi += 1;<br>&nbsp;&nbsp;&nbsp; }<br>}</pre>
<p>&nbsp;</p>
<p>2) Add to this C program as follows:</p>
<p>a) Create an array of any five doubles and use a double pointer to iterate through it and print the addresses and values in the same way as the sample code iterates through the int array.&nbsp; The printf format code for a double is %f.</p>
<p>b) Do the same with an array of any five chars (for example, char myChars = {'J', 'o', 'h', 'n'}. The format code for a char is %c.</p>
<p>c) Think about this question:</p>
<p>Suppose you had no other way to find out the size of an int, a double, or a byte (and note that, in C, these may actually vary between different compilers!)&nbsp; How could the output from your program help you answer these questions?</p>
<p>&nbsp;</p>
  
<div id="assign-to-mount-point"></div>
</div>
