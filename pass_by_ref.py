class Person:
    def __init__(self, name):
        self.name = name

def greet(customer):
    print(id(customer))
    customer.name = "Sneha"
    print(customer.name)
    print(id(customer))
    

x1 = Person("Astitva")
print(id(x1))

greet(x1)

print(id(x1))
print(x1.name)
