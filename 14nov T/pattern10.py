'''

12345678
7654321
123456
54321
1234
321
12
1

'''


for i in range(9,1,-1):
 if i%2==1:
  for j in range(1,i):
   print(j,end="")
  print()
 else:
  for k in range(i-1,0,-1):
   print(k,end="")
  print()