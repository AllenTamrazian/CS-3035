fun isLong(value: Any): Boolean
{
	return value is Long
}
enum class Color {
    RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET
}
class Monster(val name: String, val height: Int, val favColor: Color)
{
	val isNamedGodzilla: Boolean
	get() = name=="Godzilla"
	val color: Boolean
	get() = favColor==Color.BLUE
	fun heightRatio(otherMonster: Monster): Double
	{
		return height/otherMonster.height.toDouble()
	}
		
}
fun main()
{
	var input:String? = "Godzilla"
	var output = if (input != null) { input.uppercase() } else {"Nothing to print!"}
	println(output)
	input = null
	output = if (input != null) { input.uppercase() } else {"Nothing to print!"}
	println(output)

	var input1:String? = "Godzilla"
	var output1 = input1?.length
	println(output1)
	input1 = null
	output1 = input1?.length
	println(output1)
	
	var input2:String? = "Godzilla"
	var output2 = input2?.uppercase() ?: "Nothing to print"
	println(output2)
	input2 = null
	output2 = input2?.uppercase() ?: "Nothing to print"
	println(output2)

	val value: Any = 1
	val intValue: Int = 1
	println(isLong(value))
	println(isLong(intValue))
	println(isLong(intValue.toLong()))
	
	val m1 = Monster("Godzilla", 3, Color.BLUE)
	val m2 = Monster("Godzilla", 3, Color.BLUE)
	val m3 = Monster("Godzilla", 4, Color.BLUE)
	val m4 = Monster("Mothra", 5, Color.RED)
	//toString
	println(m1)
	println(m2)
	println(m3)
	println(m4)
	//isNamedGodzilla
	println(m1.isNamedGodzilla)
	println(m2.isNamedGodzilla)
	println(m3.isNamedGodzilla)
	println(m4.isNamedGodzilla)
	//heightRatio
	println(m1.heightRatio(m1))
	println(m2.heightRatio(m1))
	println(m3.heightRatio(m1))
	println(m4.heightRatio(m1))
	//==
	println(m1==m1)
	println(m2==m1)
	println(m3==m1)
	println(m4==m1)
	//===
	println(m1===m1)
	println(m2===m1)
	println(m3===m1)
	println(m4===m1)
	
}

