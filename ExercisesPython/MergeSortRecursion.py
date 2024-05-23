def mergeSort(list):
	if(len(list) <= 1):
		return list
	return merge(mergeSort(list[0:len(list)//2]), mergeSort(list[len(list)//2:]))

def merge(leftList, rightList):
	finalList=[]
	if(len(leftList) == 0):
		return rightList
	if(len(rightList) == 0):
		return leftList
	if(leftList[0] <= rightList[0]):
		return [leftList[0]] + merge(leftList[1:], rightList)
	else:
		return [rightList[0]] + merge(leftList, rightList[1:])

print(mergeSort ([]))
print(mergeSort ([-1]))
print(mergeSort ([5,-1]))
print(mergeSort ([5,-1, 42]))
print(mergeSort ([5,-1, 42, -1000]))

print(mergeSort ([""]))
print(mergeSort (["Godzilla"]))
print(mergeSort ([" ", "Godzilla"]))
print(mergeSort (["Mothra", "Godzilla"]))    
print(mergeSort (["Mothra", "Godzilla", "Jersey Devil"]))
print(mergeSort (["Mothra", "Loch Ness Monster", "Godzilla", "Jersey Devil"]))
