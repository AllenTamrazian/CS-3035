fun getArea(radius: Double): Double = Math.PI * radius * radius

fun areaOfCirclesListDecreasing(n: Int): List<Double> = if(n<=0) emptyList() else listOf(getArea(n.toDouble())) + areaOfCirclesListDecreasing(n-1)//2

fun areaOfCirclesListIncreasing(n: Int): List<Double> = if(n<=0) emptyList() else areaOfCirclesListIncreasing(n-1) + listOf(getArea(n.toDouble()))//2

fun firstElementEachPair(l: List<Pair<Any, Any>>): List<Any> = if(l.size==0) emptyList()  else listOf(l[0].first) + firstElementEachPair(l.drop(1))//6

fun main()
{
	val rangeList = (1..25).toList()
	//2
	println(areaOfCirclesListDecreasing(25))//2
	println(areaOfCirclesListIncreasing(25))//2
	
	//3
	val listOfStuff = List<Double>(25){i->getArea(i.toDouble())}
	print(listOfStuff)
	
	//4
	println(rangeList.map { getArea(it.toDouble()) })//4

	//5
	val rangeListSquared = rangeList.map { it*it }//5A
	println(rangeList.zip(rangeListSquared))//5B
	
	//6
	val p1 = Pair<String, Int> ("Godzilla", 42)
	val p2 = Pair<Int, Int> (3, 42)
	val list = listOf(p1,p2)
	println(firstElementEachPair(list))
	
	//7
	val l1 = listOf("to", "and", "because", "important", "who", "cook", "pancakes", "people")
	val l2 = listOf("me", "bye", "the reason for", "not", "where", "chef", "crepes", "batter", "extra")
	println((l1.filter{it.length > 4}).zip(l2.filter{it.length > 4}))
	
	//8
	val l = listOf("Moe", "Curley", "Larry", "Shemp", "Groucho", "Harpo", "Beppo", "Zeppo")
	val filteredList = l.filter{it.contains('r')}
	print(filteredList)
	
}
