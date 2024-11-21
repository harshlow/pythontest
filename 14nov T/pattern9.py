'''

*
* *
* * * *
* * * * * * * 
* * * * * * * * * * * * * * * *
1+2+4+7+11+16

'''

sum,a=0,1
for i in range(0,7):
 sum=sum+a
 for j in range(i,sum):
  print("*",end="")
 a+=1
 print()