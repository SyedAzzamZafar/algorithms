import sys

# limit = sys.getrecursionlimit()
# print(f'before: {limit}')
temp_limit = 200
sys.setrecursionlimit(temp_limit)
print(sys.getrecursionlimit())

#def countdown(n):
# 	if n<=0:
# 		print('Blastoff!')
# 	else:
# 		print(n)
# 		countdown(n-1)

# countdown(5)


#Maximum Recursion Limit Exceeded
#StackOverFlow
def recurse(n, s):
	
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)



recurse(3, 0)


