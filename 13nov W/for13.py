#Wap to print series of prime number between two limit

slimit=int(input("enter a starting limit\n"))
elimit=int(input("enter a ending limit\n"))

for n in range(slimit,elimit+1):

 flag=True
 for i in range(2,n):
  if n%i==0:
   flag=False
   break

 if flag==True:
  print(n)