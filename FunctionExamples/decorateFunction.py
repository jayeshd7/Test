#A decorator is a function that takes a function as
#its only parameter and returns a function.
#This is helpful to “wrap” functionality with the same code over and over again.
#For example, above code can be re-written as following.

def welcome(fun):
    def nestedWelcome(site_name):
        return "welcome "+fun(site_name)
    return nestedWelcome
@welcome
def site(site_name):
    return site_name
print(site("jayesh"))


# decorators can be useful attach data

def attach_data(func):
    func.data = 3
    return func
@attach_data
def add(x,y):
    return x+y
print(add(2,3))
print(add.data)