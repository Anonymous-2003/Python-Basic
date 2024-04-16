class MyClass:
    a = 10
    def sum(self): # self is mandatory for methods inside class
        print("Inside sum function")
    def __init__(self): # making constructor,(self i.e one argument) is mandatory
        print("Inside constructor")
    def mul(self):
        self.c=self.a*self.a  # we have to use self to create new variable inside methods
        print(self.c)

obj = MyClass()   # creating object
                  # constructor is automatically called when the object is created
print(obj.a)
obj.sum()
obj.mul()
