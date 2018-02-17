from collections import OrderedDict

dict = {'Name': 'jayesh','Age':28}
print (str(dict))
print(dict.items())
print(len(dict))
dict1 = {}
dict1 = dict.copy()
print(dict1)
dict2 = {'id':106211}
sequ = ('Name', 'Age','ID')
dict.update(dict2)
print(dict)
if dict.keys().__contains__("abc"):
    print(dict.get("Name"))
    print("Key is available")
else:
    print(dict.setdefault("abc","123"))
    print("Key is not there")

od = OrderedDict()
od['a'] = 1
od['c'] = 3
od['b'] = 2
for key,values in od.items():
    print(key,values)

d = {}
d['a'] = 1
d['c'] = 3
d['b'] = 2
for key,values in d.items():
    print(key,values)