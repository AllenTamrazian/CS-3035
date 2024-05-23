def iterativeBinarySearch(inputList, key):
	if(len(inputList) < 1):
		return -1
	low = 0
	high = len(inputList) - 1
	mid = 0
	print("Searching" + str(inputList) + " for " + str(key))
	while(low <= high):
		mid = ((low + high) // 2)
		print("Comparing " + str(key) + " and " + str(inputList[mid]))
		if(inputList[mid] == key):
			return mid
		if(inputList[mid] < key):
			low = mid + 1
		else:
			high = mid - 1
	return -1

arr = [ 2, 3, 4, 10, 20, 21, 22, 30, 40 ]
print(iterativeBinarySearch(arr, 10))
print(iterativeBinarySearch(arr, 5))
arr2 = []
print(iterativeBinarySearch(arr2, 5))
