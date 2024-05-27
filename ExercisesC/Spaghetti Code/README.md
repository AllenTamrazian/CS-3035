<h1 class="page-title">UNGRADED Exercise: Translate Spaghetti Code</h1>
<p>Consider the code on the lecture slide titled "Spaghetti Code With Line Numbers." &nbsp;Rewrite it in C, with function calls from main to get the results for several different radii (plural of radius!) and, of course, without using goto.</p>
<div id="assign-to-mount-point"></div>

<h2>Spaghettic Code with Line Numbers</h2>
<div>
10 LET P = 3.1416
20 LET r = 2
30 LET x = 50
40 GOTO 140
50 LET r = 6
60 LET x = 80
70 GOTO 140
80 LET r = 11
90 LET x = 110
100 GOTO 140
110 END
140 LET c = r * 2 * P
150 PRINT "circumference of circle with radius "; r; " is "; c
160 GOTO x
</div>
