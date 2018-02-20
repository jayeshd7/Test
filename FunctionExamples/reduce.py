import functools
import operator

lis = [1,2,3,4,5]
print(functools.reduce(lambda x,y : x+y,lis))
print(functools.reduce(lambda a,b : a if a > b else b, lis))
print(functools.reduce(operator.add,lis))
print(functools.reduce(operator.mul,lis))