<div class="description user_content enhanced" data-resource-type="assignment.body" data-resource-id="1749137"><p><strong><span style="font-size: 24pt;">Implement a Priority Queue in Python:</span></strong></p>
<p>I. Write a Python Entry class that meets these specifications:</p>
<ul>
<li>__init__ uses parameters to set values for the instance variables self._priority and self._value</li>
<li>set_priority uses a parameter to set the priority for the entry</li>
<li>get_priority returns the priority for the entry</li>
<li>get_value returns the value for the entry</li>
<li>__str__ returns a string like this: Priority: 4; Value: Eat</li>
</ul>
<p>&nbsp;</p>
<p>II. Write a Python PQ class that meets these specifications.&nbsp; You may assume that the value has a type that you can compare using the ==, &lt;, and &gt; operators, like like a numeric type or string.</p>
<ul>
<li>__init__ creates an empty list that will hold the entries</li>
<li>add uses two parameters called priority and value to create an Entry and add it to the list</li>
<li>remove_min finds the entry with the lowest priority (or, if there is more than one entry with the lowest priority, one of them), removes it from the list, and returns a reference to it</li>
<li>set_priority takes parameters for the value and a new priority and, if there are any entries with the specified value, sets the priority for all of them to the new priority.&nbsp; Make sure that removeMin works correctly for entries whose priorities you have changed.</li>
<li>size returns the length of the list</li>
</ul>
<p>&nbsp;</p>
<p>III. Use this testing code without changes:</p>
<p>pq = PQ()<br>pq.add(2, "Eat")<br>pq.add(0, "Study for CS 3035")<br>pq.add(3, "Sleep")<br>pq.add(1, "Maintain Personal Relationships")<br>pq.add(4, "Practice Good Personal Hygiene")<br>pq.set_priority("Practice Good Personal Hygiene", 2)<br>pq.set_priority("Eat", 4)</p>
<p>while pq.size() &gt; 0:<br>&nbsp; &nbsp; print(pq.remove_min()) &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp;</p>
<p><strong>Turn in your code in a single .py file, and also turn in the output from running the testing code </strong></p></div>