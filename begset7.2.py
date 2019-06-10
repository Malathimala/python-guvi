# malathi
number=input()

count=0

for i in number:

    if((i=='0') or (i=='1')):

        count=count+1

if(count==len(number)):

    print("yes")

else:

    print("no")
