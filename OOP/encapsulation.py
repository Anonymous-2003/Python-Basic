class A:
    __a="Hello"  #a is private variable.Private variable is made by __
    def __init__(self):
        self.name=""
        print(self.__a)
        self.__show()
    def getname(self):
        return self.name
    def setname(self,n):
            self.name=n
    def __show(self): # private method is created
         print("Inside show function")
obj = A()
obj.setname("Avishek")
print(obj.getname())
# print(obj.__a) --> throws error as 'a' is private variable   
# to print private variable/methods we have to use constructor

 