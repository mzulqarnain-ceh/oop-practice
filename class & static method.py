# Ab tak jo methods likhe hain wo sab "instance methods" the — yani self lete the aur specific object ke data pe kaam
# karte the. Ab do naye types dekhte hain: Class methods aur static methods
# class method uses data of class not the object (Class ka data use kare, object ka nahi)
# we type cls instead of self, cls represents the whloe class 
# class Student:
#     school_name="City School" # Class variable - sab students ka same
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def change_school(cls,new_name):
#         cls.school_name=new_name # Poori class ka data badla
# Abi k lye is class method jo k nichy ha iska koi use nai ha is code ma
#     @classmethod
#     def from_string(cls,data): # "Ali-90" string sy object banao
#         name,marks=data.split("-")
#         return cls(name) # new object return krta ha 
# s1=Student("Ali")
# s2=Student("Umar")
# print (Student.school_name) # city school
# Student.change_school("Star School")
# print(s1.school_name) # Star school - dono ka change ho gya name
# print(s2.school_name) # Star school

# Static mehtod @staticmethod — Na self, na cls — bas ek utility function
# Class se related hota hai lekin kisi bhi object ya class ke data pe depend nahi karta:
# class MathHelper:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def is_even(n):
#         return n % 2 ==0
# print(MathHelper.add(5,9))
# print(MathHelper.is_even(8))
# print(MathHelper.is_even(9))
# Object banane ki zaroorat nahi — seedha class se call karo.

# difference between 3
# class Demo:
#     class_var="I am in class"
#     def instance_method(self): # object chye
#         print(self.class_var)
#     @classmethod
#     def class_method(cls): # class chye object nai
#         print(cls.class_var)
#     @staticmethod
#     def static_method(): # Kuch nai chye
#         print("I am independent")
# d = Demo()
# d.instance_method() # Object se call
# Demo.class_method() # class se call
# Demo.static_method() # class se call

# Test
class Temprature:
    def __init__(self,celcius):
        self.celcius=celcius
    @staticmethod
    def is_freezing(celcius):
        if celcius<=0:
            return f"Freezing! Temprature is {celcius}°C"
        else:
            return f"Normal Temprature {celcius}°C"
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return f"{(celcius * 9/5) + 32:.2f}"
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celcius=f"{(fahrenheit - 32) * 5/9:.2f}"
        return cls(celcius)
    def __str__(self):
        return f"Temprature: {self.celcius}°C"
celcius=int(input("Enter the temprature: "))
print(Temprature.is_freezing(celcius))
print(Temprature.celcius_to_fahrenheit(celcius))
t1=Temprature.from_fahrenheit(40)
print(t1)
t=Temprature(celcius)
print(t)