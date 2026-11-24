# Polymorphism



# 1. Method Overriding
class Parent:
    def dna(self):
        return "Parent DNA" 

class Child(Parent):
    def dna(self):
        return "Child DNA"

obj = Child()

print(obj.dna())


# 2. Method Overloading
class Geometry:
    def area(self, radius):
        return 3.14 * radius * radius

    def area(self, l, b):
        return l * b

obj = Geometry()
obj.area(4)



# 3. Operator Overloading

print(5 + 3)          # 8        (addition)
print("Hi " + "there")  # Hi there (concatenation)
print([1, 2] + [3])   # [1, 2, 3] (list merge)
print("ab" * 3)       # ababab   (repetition)
