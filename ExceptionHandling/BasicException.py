a = [1,2,4,5,6]
try:
    print("Second element= %d" %(a[1]))
    print("Fourth element %d "%(a[7]))
except IndexError:
    print("An error occured")

##Multiple Error

try:
    a = 3.5
    if a<4:
        b = a/(a-3)
    print("value of b =", b)
except(NameError,ZeroDivisionError):
    print("\n Error occured and handled")



