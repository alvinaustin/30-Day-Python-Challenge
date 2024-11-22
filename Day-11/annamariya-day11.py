"""
Author: Anna Mariya Shibu
Created On :22/11/2024

"""
from lib2to3.fixes.fix_tuple_params import tuple_name

cities=("delhi","bombay"," madurai")
print(cities[1])

fruits=("apple","banana","cherry")
vegetables=("carrots","cabbage")
both=fruits+vegetables
print(both)




#Here 'tuple' object does not support item assignment
My_tuple=(1,3,5,7,8)
new_tuple=My_tuple[:2]+(10,)+My_tuple[2:]
print(new_tuple)

tuple=(1,2,5,6,5,4,5)
print(tuple.count(5))
tuple=(1,2,3,4,5)
print(tuple.index(5))