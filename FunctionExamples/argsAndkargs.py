#*args allows you to do is take in more arguments than the
# number of formal arguments that you previously defined.
# With *args, any number of extra arguments can be tacked on to your current
# formal parameters (including zero extra arguments).

def testify(arg1, *argv):
    print("first argument :", arg1 )
    for arg in argv:
        print("Next argument through *argv :" , arg)


testify('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#**kwargs in function definitions in python is used to pass a keyworded,
#  variable-length argument list. We use the name kwargs with the double star.
#  The reason is because the double star allows
#  us to pass through keyword arguments (and any number of them).


def test(**kwargs):
    if kwargs is not None:
        for key,value in kwargs.iteritems():
            print("%%s == %%s"%(key,value))
test(name="pooja")