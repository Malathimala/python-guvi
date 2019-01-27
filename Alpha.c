#include<stdio.h>
int main()
{
char ch;
printf("%c",ch);
scanf("%c",&ch);
if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z'))
{
printf("Alphabet");
}
else
{
printf("No");
}
return 0;
}
