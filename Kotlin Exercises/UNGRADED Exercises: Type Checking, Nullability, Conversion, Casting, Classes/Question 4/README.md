<h1 class="page-title">UNGRADED Exercises: Type Checking, Nullability, Conversion, Casting, Classes<button aria-haspopup="dialog" class="ally-accessible-versions ally-add-tooltip" data-id="page:1792524" data-ally-content-id="page:1792524" data-ally-richcontent-eid="page:1792524" aria-label="Alternative formats" title="Alternative formats"></h1>
  
<p>4)</p>
<p>Copy this code to create a color Enum:</p>
<p>enum class Color {<br>&nbsp; &nbsp; RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET<br>}</p>
<p>&nbsp;</p>
<p>Then create a Monster data class.&nbsp;</p>
<ul>
<li>A monster has a name, a height, and a favorite color.&nbsp;</li>
<li>The class should also have a property called isNamedGodzilla, with an accessor that will return true if the monster is named Godzilla, else false.&nbsp; See the lecture slide with a Rectangle class with a property isSquare.</li>
<li>The class should also have a heightRatio function, which takes another Monster as a parameter and returns the ratio of the instance monster's height to that of the parameter Monster.&nbsp;</li>
</ul>
<p>Write a main() that creates four monsters:</p>
<ul>
<li>A Monster named Godzilla with some values for height and favorite color</li>
<li>Another Monster also named Godzilla and with the same height and favorite color</li>
<li>Another Monster named Godzilla but with a different height</li>
<li>Another Monster with completely different data</li>
</ul>
<p>For each of the monsters, "print" the Monster (you will get the toString()).&nbsp; Then print the results of the following:</p>
<ul>
<li>calling isNamedGodzilla() on the Monster</li>
<li>calling heightRatio on the first Godzilla and sending the current one as a parameter (for example, if the first Godzilla is m1, then m1.heightRatio(m1) should return 1.0)</li>
<li>calling == (equals in the sense of the equals method) on the first Godzilla and the current Monster</li>
<li>the result of running === (equals in the sense of the same object in memory) on the original Godzilla and the current Monster&nbsp;</li>
</ul>
  
<div id="assign-to-mount-point"></div>
</div>
