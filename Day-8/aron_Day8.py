"""
Author:Aron Bobby Daniel
Date:16-11-2024
"""

# Using a for loop to print numbers from 1 to 100
for i in range(1,101):
    print(i,end=' ')

# Using a while loop to print numbers from 1 to 50
i=0
while i<50:
    i+=1
    print(i)


# Example of using break and continue
i=0
for i in  range(1,10):
    if i==10:
        break
    if i==7:
        continue
    print(i,end=' ')

