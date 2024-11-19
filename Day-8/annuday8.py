'''
author name:Annu James
date:16/11/24
'''
for i in range(1,10):
    print(i)
    i=5
while i<=12:
    i+=1
    print(i)
i=0
for i in range(1,25):
    if i==12:
       break
    if i==6:
      continue
    print(i,end='')
