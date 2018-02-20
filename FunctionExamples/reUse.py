class Person(object):
    def __init__(self ,name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Jayesh")
print(emp.getName(),emp.isEmployee())

emp = Employee("Pooja")
print(emp.getName(),emp.isEmployee())


class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)