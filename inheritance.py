# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} is eating!!!")
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking!!!")
# my_dog=Dog("Tommy")
# my_dog.bark()
# my_dog.eat()

# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def show(self):
#         print(f"Name: {self.name} | Breed: {self.breed}")
# d=Dog("Tommy", "German Shepherd")
# d.show()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}")
class Student(Person):
    def __init__(self,name,age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks
    def show_detail(self):
        self.introduce()
        # print(f"Name: {self.name} | Age: {self.age} | Roll No: {self.roll_no} | Marks: {self.marks}")
        print(f"Roll No: {self.roll_no} | Marks: {self.marks}")
s1=Student("ALi",12,1,87)
# s1.introduce()
s1.show_detail()
s2=Student("Mavrik",10,2,95)
# s2.introduce()
s2.show_detail()
