class Cat:
    def sound(self):
        print("Meow")
class Dog:    
    def sound(self):
        print("Woof")
# def make_sound(animal_object):
#     animal_object.sound()
cat=Cat()
dog=Dog()
# make_sound(cat)
# make_sound(dog)
cat.sound()
dog.sound()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name} | Marks: {self.marks}"

s = Student("Ali", 90)
print(s)  # Student: Ali | Marks: 90