<div class="description user_content enhanced" data-resource-type="assignment.body" data-resource-id="1749522"><p>Implement a Queue ADT in Python two different ways: a) using the built in Python List and b) using a linked list class you code yourself.&nbsp; I suggest you complete Part 1 and test it before proceeding to part 2.</p>
<p>Part 1:</p>
<p>1a (10 points) Code a SinglyLinkedListNode class. This class must have a variable for the data value and one that is a reference to the next node in the list, with getters and setters, an __init__, and a reasonable __str__</p>
<p>1b (20 points) Code the SinglyLinkedList class. It should have</p>
<ul>
<li>an __init__,</li>
<li>instance variables for start and end (the first and last nodes), and the size of the list, and getters (but not setters) for start and end</li>
<li>methods to add nodes at the beginning and at the end, each of which takes the data element, creates a node with that data element, and adds it in the appropriate place, does whatever is necessary with the start and end variables, and increments the size variable</li>
<li>methods to delete the first and last nodes, which should also do whatever is necessary with the start and end variables and decrement the size variable.</li>
<li>a&nbsp; __len__ method that returns the length of the list.&nbsp; Giving this method this name will cause it to override the len() operator; that is, calling len(myList) will get the length of the list.</li>
<li>You may want to write a method that traverses the list and prints all the data elements, to assist you in debugging.</li>
</ul>
<p>Be sure that the add methods work correctly when called on and empty list, and that the delete methods do nothing when called on an empty list.</p>
<p>there are several methods that are typically part of linked list classes, but that this assignment does not require.&nbsp; These include contains(), methods to add and delete at arbitrary indices, and several others.</p>
<p>Part 2</p>
<p>2a (15 points) Code the AbstractQueue class.&nbsp; See the lecture notes to see how to write an abstract class in Python.&nbsp; This abstract class will need abstract offer (add to the back of the queue), poll (remove from the front of the queue and return a reference to the object removed), peek (just return a reference to the object at the front without removing it from the queue), and __len__ methods. Use the names offer and poll, rather than enqueue and dequeue, because I have testing code that uses these names.</p>
<p>2b (20 points) Code the Python class PythonListQueue, which use Python's built in list to implement a queue.&nbsp; This class must inherit from AbstractQueue and implement all its methods.&nbsp; Note the Python lists are implemented using underlying arrays of pointers, much like Java ArrayLists.</p>
<p>2c (20 points) Code the Python class SLLQueue, which uses your linked list class to implement a queue.&nbsp; This class must inherit from AbstractQueue and implement all its methods.</p>
<p>Part 3</p>
<p>3a (15 points) Write driver code to thoroughly test both your queue implementations.&nbsp; You may hard code the data; you do not need to take user input.</p>
<p>Turn in your code (in this case, it can be in a single .py file) and output from running your test code.</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;</p></div>
