#Wap to check entered number is prime or not

n=int(input("enter a number"))
flag=True

for i in range(2,n):
 if n%i==0:
  print("Number is not prime")
  flag=False
  break

if flag==True:
 print("prime number")