# malathi
n=int(input())
first=0
second=1
for i in range(n):
	print(second,end=" ")
	temp=first
	first=second
	second=second+temp
