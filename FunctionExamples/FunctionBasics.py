# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

def welcome(str):
    def nestedWelcome():
        return "welcome "
    return nestedWelcome() +str
def site(site_name):
    return site_name
print(welcome(site("jayesh")))