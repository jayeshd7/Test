import  collections
d = {'a' : 1 , 'b' : 2}
defd = collections.defaultdict(lambda :'key not found')
defd['a'] = '1'
print(defd['a'])
print(defd['c'])
