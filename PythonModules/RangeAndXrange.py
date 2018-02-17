import sys

## xrange is more faster than range it consume less memory


a = xrange(1,6)
print(sys.getsizeof(a))

b = range(1,6)
print(sys.getsizeof(b))