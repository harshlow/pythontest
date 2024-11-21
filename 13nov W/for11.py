#WAP to check entered number is perfect or not

n=int(input("Enter a number to check perfect\n"))

s=0
for i in range(1,n):
 if n%i==0:
  s+=i

if n==s:
 print("Perfect number")
else:
 print("Not perfect number")