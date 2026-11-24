
###########################################
####       Inheriting constructor     ####
##########################################

class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s1 = SmartPhone(2000, 'apple', '15MP')
print(s1.brand)

## If child class does not have constructor it will inherit the constructor from parent class

############################################
###       Inheriting private members    ####
############################################
class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.__brand = brand        # private member
        self.camera = camera

    def __processor(self):
        print("snapdragon")

class SmartPhone(Phone):
    pass

#s2 = SmartPhone(2000, 'apple', '15MP')
#print(s2.__brand)
#print(s2.__processor())

# Child class can't inherit private data members/methods of parent class


##########################################
#####    Method Overriding          #####
#########################################


class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand        
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    print("inside smartphone constructor")

    def buy(self):
        print("Buying a smartphone")

s3 = SmartPhone(2000, 'apple', '15MP')
s3.buy()



##############################################
#######       super() function           #####
#############################################

class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand        
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s3 = SmartPhone(2000, 'apple', '15MP')
s3.buy()


##################################################
### super() function -> Inherit constructor   ####
##################################################

class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand        
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):

    def __init__(self, price, brand, camera, color, display):
        super().__init__(price, brand, camera)
        self.color = color
        self.display = display

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s4 = SmartPhone(2000, 'apple', '15MP', 'black', '16inch')
print(s4.price)
print(s4.camera)
print(s4.display)



              