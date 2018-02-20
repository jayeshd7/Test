class test:
    __hidden_variable = 0
    def add(self,increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)
myobj = test()
myobj.add(2)
myobj.add(10)
print(myobj._test__hidden_variable)
