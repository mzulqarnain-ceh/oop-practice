# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         print(f"{self.name} is barking Booo! Booo!")
# my_dog=Dog("tomy",5)
# # print(my_dog.name)
# # print(my_dog.age)
# my_dog.bark()

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def show_details(self):
        print(f"Name: {self.name} | Roll No: {self.roll_no} | Marks: {self.marks}")
s1=Student("Ali",1,90)
s2=Student("Anny",2,60)
s3=Student("Mario",3,68)
s1.show_details()
s2.show_details()
s3.show_details()
