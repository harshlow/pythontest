'''
12345678
8765432
345678
87654
5678
876
78
8

'''



for i in range(1,9):
 if i%2==0:
  for j in range(8,i-1,-1):
   print(j,end="")
 else:
  for j in range(i,9):
   print(j,end="")
 print()