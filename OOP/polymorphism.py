# overloading

class A:
    def showdata(self,name=''):
        print("Hello "+name)
obj = A()
obj.showdata()
obj.showdata('Avishek')

# here same function are giving two outputs i.e function overloading

#overriding
#function with same name inside parent and child class will override the base class and only call the child class function

class one:
    def show(self):
        print("Inside class one")
class two(one):
    def show(self):
        super().show()  # to call show() of base we have to use super function 
        print("Inside class two")
t = two()
t.show()    # it calls show() function of derived class i.e base class is overridden
