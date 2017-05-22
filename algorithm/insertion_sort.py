def print_list() : 
	for a in list : 
		print(str(a), end=" ")
	print()

list = [6, 8, 3, 9, 5, 2]
list_tmp = ()

#===============================
print("insertion sort start!")
print_list()
for i in range(len(list)) :
	print() 
	print("index ["+str(i)+"] : ")
	for j in range(i) : 
		if list[j] > list[i] : 
			list.insert(j, list[i])
			list.pop(i+1)
			print_list()
			break
		elif j+1 == i : 
			print_list()	
