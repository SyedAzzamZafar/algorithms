

# l = [5,3,7,1,9]
# print(l)

# def max_l(l1,l2):
# 	if len(l1)>len(l2):
# 		return l1
# 	else:
# 		return l2


# def min_l(l1,l2):
# 	if len(l1)>len(l2):
# 		return l2
# 	else:
# 		return l1



# def merge(l1=[],l2=[]):
# 	l3=[]
# 	if len(l1)==0:
# 		return l2
# 	elif len(l2)==0:
# 		return(l1)
# 	else:
# 		maxl = max_l(l1,l2)
# 		minl = min_l(l1,l2)
# 		im=0
# 		for i in range(len(maxl)):
# 			if minl[im]>maxl[i]:
# 				l3.append(maxl[i])
# 				i+=1
# 			elif minl[im]==maxl[i2]:
# 				l3.append(maxl[i])
# 				im+=1
# 				i+=1
# 			elif minl[im]<maxl[i2]:
# 				l3.append(minl[im])
# 				im+=1
# 			elif minl[im]==None:
# 				l3+maxl[i:]
# 				return(l3)
# 			elif maxl[i]==None:
# 				l3+minl[i:]
# 				return(l3)

		


# #new method	
# def merge_binary(n,m):
# 	l_unit = []
# 	if n<m:
# 		l_unit.append(n)
# 		l_unit.append(m)
# 		return(l_unit)
# 	else:
# 		l_unit.append(n)
# 		l_unit.append(m)
# 		return(l_unit)






			
# def merge_sort(l):
	
# 	if len(l)==2:
# 		l = merge_binary(l[0],l[-1])
# 		return l
# 	if len(l)==1:
# 		return(l)
# 	else:
# 		mid=len(l)//2
# 		l1,l2=merge_sort(l[:mid+1]),merge_sort(l[mid+1:])
# 		return(merge(l1,l2))

# print(merge_sort(l))

def merge_sort():








