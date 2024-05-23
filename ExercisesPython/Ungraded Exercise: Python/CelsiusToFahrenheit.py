lower=0
upper=0


def GetInput():
	return int(input("Enter a number for the value"))

def calculate(lower, upper):
	temps = range(lower, upper)
	for item in temps:
		f = item * 9.0/5.0 + 32
		print(f)
		

lower = GetInput()
upper = GetInput()
calculate(lower, upper)
