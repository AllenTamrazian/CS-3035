fun divide(a: Double, b:Double): Double
{
	return a/b
}

fun main() {
	val arrayOfMonsters = arrayOf<String>("Godzilla","Mothra","Mechatron")
	for(i in arrayOfMonsters)
	{
		println("$i")
	}
	println("Monster at index 1: "+ arrayOfMonsters.get(1))
	println("Monster at index 1: "+ arrayOfMonsters[1])
	arrayOfMonsters.set(1, "King Kong")
	for(i in arrayOfMonsters)
	{
		println("$i")
	}
	if(arrayOfMonsters.contains("King Kong"))
	{
		println("King Kong is here")
	}
	else
	{
		println("King Kong is not here")
	}
	println(divide(3.0,4.0))
	
}
