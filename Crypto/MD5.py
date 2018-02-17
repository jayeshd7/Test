import hashlib
resultset = hashlib.md5(b'jayesh')
print("The byte values is ",end="")
print(resultset.digest())
print(resultset.hexdigest())