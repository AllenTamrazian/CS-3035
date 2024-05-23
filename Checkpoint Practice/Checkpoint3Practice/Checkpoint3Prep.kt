fun isSquareRoot(a: Double, b: Double, c: Double): Boolean = if (isEq(Math.pow(a,2.0)+Math.pow(b,2.0), Math.pow(c,2.0), 0.001)) true else false

fun isEq(a: Double, b: Double, c: Double): Boolean = Math.abs(a - b) <= c

fun isPyth(a:Double,b:Double,c:Double): Boolean = if(a>b && a>c) isSquareRoot(b,c,a) else if(b>a && b>c) isSquareRoot(a,c,b) else if(c>a && c>b) isSquareRoot(a,b,c) else false

fun harm(n: Int): Double = if(n==1) 1.0 else 1.0/n + harm(n-1)

fun sideEffectsNoTransparency(a:Int,b:Int): Int
{
	print(a)
	return a+b
}

fun sideEffectsButTransparency(a:Int,b:Int):Int
{
	print(a)
	var total = a+b
	return total
}

fun noSideEffectsNoTransparency(a:Int,b:Int): Int
{
	return a+b
}

fun noSideEffectsButTransparency(a:Int,b:Int): Int
{
	var total = a+b
	return total
}

fun pythTriplesUnder20()
{
	for(i in 1..19)
	{
		for(j in 1..19)
		{
			for(k in 1..19)
			{
				if(isPyth(i.toDouble(), j.toDouble(), k.toDouble())==true)
				{
					println(i.toString()+" "+j.toString()+" "+k.toString())
				}
			}
		}
	}
}
fun main()
{
	val smallest = 3.0
	val medium = 4.0
	val biggest = 5.0
	println(isSquareRoot(smallest, medium, biggest))
	println(isSquareRoot(smallest, biggest, biggest))
	println(isPyth(biggest,smallest,medium))
	println(isPyth(smallest,biggest,medium))
	println(isPyth(smallest,medium,biggest))
	println(harm(3))
	pythTriplesUnder20()
}
