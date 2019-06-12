# malathi
import math
n,m=map(int,input().split())
k=(n*m)
q=int(math.sqrt(k))
if(k==q*q):
	print("yes")
else:
	print("no")
