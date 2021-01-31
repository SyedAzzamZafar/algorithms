filename = 'day1input.txt'
with open(filename,'r') as f:
	lines = [int(n) for n in f.read().split('\n') if n!='']

#print(lines)

for index in range(1,len(lines)):
	value = lines[index]
	prev_index = index - 1
	while prev_index>=0 and lines[prev_index]>value:
		lines[prev_index+1] = lines[prev_index]
		lines[prev_index] = value
		prev_index-=1

print(lines)


###Recursive###

def rec_ins_sort(lines):
	k = len(lines)
	if 
		
