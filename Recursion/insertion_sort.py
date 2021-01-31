
arr = [3,7,1,5,9]


# for index in range(1,len(input_array)):
# 	if input_array[index]<input_array[index-1]:
# 		cmpi = index
# 		while cmpi!=0:
# 			if input_array[cmpi]<input_array[cmpi-1]:
# 				input_array[cmpi],input_array[cmpi-1]=input_array[cmpi-1],input_array[cmpi]
# 			cmpi-=1
# 	else:
# 		continue


# for index in range(1,len(arr)):
# 	i = index
# 	while i!=0 and arr[i]<arr[i-1]:
# 		(arr[i],arr[i-1]) = (arr[i-1],arr[i])
# 		i-=1

def insert(arr,index):
	i = index
	if i>0 and arr[i]<arr[i-1]:
		(arr[i],arr[i-1])=(arr[i-1],arr[i])
		return(insert(arr,index-1))
	else:
		return



for index in range(1,len(arr)):
	insert(arr,index)





# for index in range(1,len(input_array)):
# 	comp_i = index
# 	while comp_i>0 :
# 		if input_array[comp_i]<input_array[comp_i-1]:
# 			(input_array[comp_i],input_array[comp_i-1])\
# 			=(input_array[comp_i-1],input_array[comp_i])
# 		comp_i-=1



	
print(arr)
