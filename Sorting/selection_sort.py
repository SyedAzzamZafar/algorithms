filename = 'day1input.txt'
with open(filename,'r') as f:
	lines = [int(num) for num in f.read().split('\n') if num!='']


#print(lines)

# del lines[-1]

# for num in lines:
# 	print(num)


start = 0
while(start!=len(lines)):
	#minm = 2020
	m_i = start
	for i in range(start+1,len(lines)):
		if lines[i]<lines[m_i]:
			m_i = start

	lines[start],lines[m_i] = lines[m_i],lines[start] 

	#print(minm,start,lines[start])
	
	#print(minm,lines[start])
	start+=1






# for num in lines:
# 	print(num)

