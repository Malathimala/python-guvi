# mala
n=int(input())
sum=0
while n:
    a=n%10
    sum=sum+(a*a)
    n//=10
print(sum)
