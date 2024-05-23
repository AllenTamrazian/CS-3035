fun highMethod(n:Int, f:(Int)->Int):Int = f(f(n))

fun square(n:Int):Int = n*n

fun main()
{
	println(highMethod(2,::square))
	println(highMethod(-5, {it->it*2}))
}
