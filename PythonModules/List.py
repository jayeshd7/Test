import sys

power_of_2 = [2 ** x  for x in range(1,9)]
print(power_of_2)
string = "My number is 9229956621"
find_number = [x for x in string if (x.isdigit())]
print(find_number)

a = 5
table = [[a,b ,a*b ]for b in range(1,11)]
for i in table:
    print(i)
lst = range(1,11)
print(lst)
lst_1 = lst[1 : 5]
print(lst_1)
lst_rev = lst[9: 4: -2]
print(lst_rev)

lst_odd = filter(lambda x : x%2 == 1,range(1,10))
print(lst_odd)