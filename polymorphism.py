# class Dog:
#     def sound(self):
#         print("Bhoo Bhoo!")
# class Cat:
#     def sound(self):
#         print("Meow Meow!")
# class Cow:
#     def sound(self):
#         print("Moo Moo!")
# animals=[Dog(),Cat(),Cow()]
# for animal in animals:
#     animal.sound()

# class Shape:
#     def area(self):
#         print("Area is calculating")
# class Circle(Shape): #inherit
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self): #overriding parent's method
#         print(f"Area of Circle is: {3.14*self.radius**2}")
# class Rectangle(Shape): #inherit
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self): #overriding parent's method
#         print(f"Area of Rectangle is: {self.length * self.width}")
# s=[Shape(),Circle(5),Rectangle(4,6)]
# for a in s:
#     a.area()

class Vehicle:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def describe(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def describe(self):
        print(f"{self.name} is a Car | Speed: {self.speed} | Fuel: Petrol")
class Bike(Vehicle):
    def describe(self):
        print(f"{self.name} is a Bike | Speed: {self.speed}")
        # print("Bike can carry 1 or 2 person")
class Truck(Vehicle):
    def describe(self):
        print(f"{self.name} is a Truck | Speed: {self.speed}")
        # print("Truck is used for heavy loads")
v=[Vehicle("Vehicle",80),Car("toyota",120),Bike("CG150",100),Truck("Volks",60)]
for t in v:
    t.describe()