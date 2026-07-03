# methods that are start and end with double underscore are called dunder methods,these are special methods which python automatically calls under certain situations
# __str__ used for print object, when you directly print object it automatically calls __str__method

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return f"Student: {self.name} | Marks: {self.marks}"
# s=Student("ali",86)
# print(s)
# without __str__ method the output will look like this <__main__.Student object at 0x0000017B83E186E0>

# __len__ method
# class Playlist:
#     def __init__(self,songs):
#         self.songs=songs
#     def __len__(self):
#         return len(self.songs)
# p=Playlist(["Song A","Song B"])
# print (len(p))

# __add__ add two objects with +
# class Bag:
#     def __init__(self,items):
#         self.items=items
#     def __add__(self,other):
#         combined = self.items + other.items
#         return Bag(combined)
#     def __str__(self):
#         return f"Bag items: {self.items}"
# b1=Bag(["Books","Pen"])
# b2=Bag(["Bottle","Lunch"])
# b3=b1+b2 # __ad__ method call ho ga
# print(b3)

# __eq__ comparing two objects
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __eq__(self, other):
#         return self.marks==other.marks # marks compre kary ga
# s1=Student("Ali",90)
# s2=Student("Aliyan",90)
# print(s1==s2) # True ay e ga kyu k marks same hain dono k 90 hain

# test
# class ShoppingCart:
#     def __init__(self,owner,items=None):        
#         self.owner=owner
#         self.items= items or []
#     def add_item(self,item,price):
#         self.items.append({"item":item, "price":price})
#     def __str__(self):
#         return f"Owner: {self.owner} | Total Items: {self.items}"
#     def __len__(self):
#         return len(self.items)
#     def __add__(self,other):
#         combined=self.items+other.items
#         return ShoppingCart(self.owner,combined)
# s=ShoppingCart("Ali")
# s.add_item("Item_1","40pkr")
# s.add_item("Item_2","90pkr")
# s1=ShoppingCart("Haider")
# s1.add_item("Item_3","100pkr")
# s3=s1+s
# print (s)
# print (len(s))
# print(s3)

# again test
class ShoppingCart:
    def __init__(self,owner,items=None):
        self.owner=owner
        self.items=items or []
    def add_item(self,item,price):
        self.items.append({"item":item, "price":price})
    def __str__(self):
        return f"Owner: {self.owner} | Total Items: {self.items}"
    def __len__(self):
        return len(self.items)
    def __add__(self,other):
        combined=self.items+other.items
        return ShoppingCart(self.owner,combined)
s1=ShoppingCart("Ali")
s1.add_item("Apple","50pkr")
s1.add_item("Banana","100pkr")
print(s1)
print(len(s1))
s2=ShoppingCart("Qasim")
s2.add_item("Mango","300pkr")
s3=s1+s2
print(s3)