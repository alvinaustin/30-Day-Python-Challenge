"""
Author:Aron Bobby Daniel
Date:23-11-2024
"""

my_tuple=("newyork","pattikkad","kunnamkulam")
print(my_tuple[1])

fruits=("Apple","Watermelon")
vegetables=("Brinjal","Potato")
concatenate=fruits+vegetables
print(concatenate)

"""
tuple1=(1,2,3,4,5)
tuple1[2]=20
print(tuple1)  #gives an error because tuple is immutable
"""
## Create a new tuple by concatenating existing tuples

tuple1=("apple","orange","pineapple","watermelon")
new_tuple=tuple1[:2]+("Pear","guava")+tuple1[2:]
print(new_tuple)

tuple_count=(1,2,3,4,5,3,4,5,5,6,7,2,5,6,5)
print(tuple_count.count(5))

tuple_index=(1,3,7,4,5,6,7,8,9,0,78)
print(tuple_index.index(7))