from datetime import date

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthyear(cls,name,year):
        return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):
        return age >18
p = person("jayesh",28)
p1 = person.fromBirthyear("jayesh",1991)

print(p.age)
print(p1.age)

print(person.isAdult(28))