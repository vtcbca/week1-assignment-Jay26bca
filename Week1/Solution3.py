n=int(input("Enter number:"))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("the number is a palindrome")
else:
    print("the number isn't a palindrome")