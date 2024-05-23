import re
def letterCount(stringToCount, count):
	if(len(stringToCount) == 0):
		print(count)
	else:
		stringToCount = stringToCount[1:]
		letterCount(stringToCount, count+1)
		
def reverseString(stringToReverse, reversedString):
	if(len(stringToReverse) == 0):
		print(reversedString)
	else:
		reversedString = reversedString + stringToReverse[-1]
		stringToReverse = stringToReverse[:-1]
		reverseString(stringToReverse, reversedString)
		
def isPalindrome(stringToCheck):
	stringToCheck = re.sub(r'[^\w\s]','',stringToCheck).replace(" ", "").lower()
	if((len(stringToCheck) == 1) or (len(stringToCheck) == 0)):
		print(True)
	else:
		if(stringToCheck[0] == stringToCheck[-1]):
			stringToCheck=stringToCheck[1:]
			stringToCheck=stringToCheck[:-1]
			isPalindrome(stringToCheck)
		else:
			print(False);
	
letterCount("hid",0)
reverseString("hid","")
isPalindrome("Madam, I'm Adam")
