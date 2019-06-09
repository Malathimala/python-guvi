# malathi
a=str(input())

c=0

d=0

for i in a:

    if(i.isalpha()):

       c=c+1

    elif(i.isnumeric()):

       d=d+1

if(c>=1 and d>=1):

    print("Yes")

else:

    print("No")
