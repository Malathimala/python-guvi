# malathi
n=str(input())
l=[]
for i in n:
	if(i.isdigit()):
	    l.append(i)
print(*l,sep="")
