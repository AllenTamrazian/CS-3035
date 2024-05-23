fun summation(n: Int): Int
{
	return if (n == 0) {
	0
	} else {
	n + summation(n - 1)
	}
}
fun summationEB(n: Int):Int = if(n==0) 0 else n + summation(n - 1)

fun fibonacci(n: Int):Int = if(n==0) 0 else if (n==1) 1 else fibonacci(n-2) + fibonacci(n - 1)

fun isPyth(a:Double,b:Double,c:Double): Boolean = if(a>b && a>c) Math.abs(Math.pow(b,2.0) + Math.pow(c,2.0) - Math.pow(a,2.0)) <= 0.001 else if(b>a && b>c) Math.abs(Math.pow(a,2.0) + Math.pow(c,2.0) - Math.pow(b,2.0)) <= 0.001 else if(c>a && c>b) Math.abs(Math.pow(a,2.0) + Math.pow(b,2.0) - Math.pow(c,2.0)) <= 0.001 else false

fun recursivePalindromeEB(stringTest: String): Boolean = if(stringTest.length < 2) true else if(stringTest[0]!=stringTest[stringTest.length-1]) false else recursivePalindromeEB(stringTest.substring(1,stringTest.length-1))

fun recursivePalindrome(stringTest: String): Boolean
{
	return if(stringTest.length < 2)
	{
		true 
	}
	else if(stringTest[0]!=stringTest[stringTest.length-1])
	{
		false 
	}
	else 
	{
		recursivePalindromeEB(stringTest.substring(1,stringTest.length-1))
	}
}

fun main()
{
	val number = 5
	val summation = summation(number)
	println("The summation of $number is $summation")
	
	val summationEB = summationEB(number)
	println("The summationEB of $number is $summationEB")
	
	val fib = fibonacci(number)
	println("The fibonacci sequence of $number is $fib")
	
	val smallest = 3.0
	val medium = 4.0
	val biggest = 5.0
	println(isPyth(biggest,smallest,medium))
	println(isPyth(smallest,biggest,medium))
	println(isPyth(smallest,medium,biggest))
	val ss = listOf("", "A", "AA", "AB", "AAA", "ABA", "ABB", "AAAA", "AABA", "ABBA", "ABCBA", "ABCAB")
	for (stringToCheck in ss)
	{
		println(recursivePalindromeEB(stringToCheck))
	}
	for (stringToCheck in ss)
	{
		println(recursivePalindrome(stringToCheck))
	}
}
