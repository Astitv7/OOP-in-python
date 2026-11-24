# Q1 

class Parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, val, num):
        self.__val = val

    def get_val(self):
        return self.__val

son = Child(100, 20)
print("Child val", son.get_val())
print("Parent Num:", son.get_num())

# Q2 
class A:

    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("class A", self.var1 )

class B(A):
    def display2(self, var1):
        print("class B", self.var1 )

obj = B()
obj.display1(200)




# Q3
