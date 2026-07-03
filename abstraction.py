# from abc import ABC , abstractmethod
# class Shape(ABC): # Abstract class
#     @abstractmethod
#     def area(self): # Abstract method - has no body, you have to define them in child class
#         pass
#     @abstractmethod
#     def perimeter(self): # Abstract method - has no body, you have to define them in child class
#         pass
# class Circle(Shape): # Inherit
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(f"Area of Circle is: {3.14*self.radius**2:.1f}")
#     def perimeter(self):
#         print(f"Perimeter of Circle is: {2*3.14*self.radius:.1f}")
# class Rectangle(Shape): # Inherit
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(f"Area of Rectangle is: {self.length*self.width:.1f}")
#     def perimeter(self):
#         print(f"Perimeter of Ractangle is: {2*(self.length+self.width):.1f}")
# class Triangle(Shape):
#     pass
# try:
#     t=Triangle()
# except Exception as e:
#     print(e)
# # s=Shape() # This gives error because abstract class ha no object
# c=Circle(5)
# c.area()
# c.perimeter()
# r=Rectangle(4,6)
# r.area()
# r.perimeter()

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def show_info(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
    def calculate_salary(self):
        print(f"Your Salary is: {self.salary}")
    def show_info(self):
        print(f"Your name is: {self.name} and your salary is: {self.salary}\n")
class PartTimeEmployee(Employee):
    def __init__(self,name,hour_worked,hourly_rate):
        self.name=name
        self.hour_worked=hour_worked
        self.hourly_rate=hourly_rate
    def calculate_salary(self):
        print(f"Your salary is: {self.hour_worked*self.hourly_rate}")
    def show_info(self):
        print(f"Your name is: {self.name}")
        self.calculate_salary()
        print("\n")
        # print(f"Your name is: {self.name} and your salary is: {self.hour_worked*self.hourly_rate}")
class Freelancer(Employee):
    def __init__(self,name,projects_completed,payment_per_project):
        self.name=name
        self.projects_completed=projects_completed
        self.payment_per_project=payment_per_project
    def calculate_salary(self):
        print(f"Your Salary is: {self.projects_completed*self.payment_per_project}")
    def show_info(self):
        print(f"Your name is: {self.name} and your salary is: {self.projects_completed*self.payment_per_project}")
f=FullTimeEmployee("ALi",50000)
f.calculate_salary()
f.show_info()
p=PartTimeEmployee("Qasim",60,15)
p.calculate_salary()
p.show_info()
frelancer=Freelancer("Hadi",10,100)
frelancer.calculate_salary()
frelancer.show_info()