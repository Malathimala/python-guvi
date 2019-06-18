# malathi
p=int(input())

j=list(map(int,input().split()))

j.sort()

m=0

z=0

for i in range(len(j)):

    if j[i]>=m:

        z=z+1

    m=m+j[i]

print(z)
