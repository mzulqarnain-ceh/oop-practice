# old method without property
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,value):
#         self.__marks=value
# s=Student(90)
# print(s.get_marks()) # get krna para
# s.set_marks(95) # set krna para
# print(s.get_marks())

# new method with property
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     @property
#     def marks(self):  # getter
#         return self.__marks
#     @marks.setter
#     def marks(self,value):  # setter
#         if value < 0 or value > 100:
#             print("Invalid Marks")
#         else:
#             self.__marks=value
# s=Student(90)
# print(s.marks)  # Attribute ki tarah access kiya ha, () nai lagi methods ki tarah
# s.marks=95      # Attribute ki tarah set kiya ha, method nai lagaya ha 
# s.marks=109     # Invalid marks
# print(s.marks)  # 95 - change nai huwa kyu k 109 bara ha 100 sy

# @property agr setter na likho tu variable read only ban jata ha 
# class Circle:
#     def __init__(self,radius):
#         self.__radius=radius
#     @property
#     def area(self):
#         return 3.14 * self.__radius ** 2
# c=Circle(5)
# print(c.area)
# c.area=100 # Error aa ey ga setter nai ha 

# test
class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    @property
    def bankbalance(self):  # getter
        return self.__balance
    @bankbalance.setter
# Python mein setter ka naam property ke naam se same hona chahiye:
    def bankbalance(self,balance_value):   # setter
        if balance_value < 0:
            print("Invalid balance!")
        else:
            self.__balance=balance_value
    def deposit(self,amount):
        if amount<=0:
            print("Please enter a valid amount to deposit")
        else:
            self.__balance+=amount
    def withdraw(self,amount):
        if amount<=0 or amount>self.__balance:
            print(f"Please enter a valid amount to withdraw, your current balance is {self.__balance}")
        else:
            self.__balance-=amount
    def __str__(self):
        return f"Account: {self.owner} | Balance: {self.__balance}"
a=Bank("Ali",100)
print(a)
print(a.bankbalance)
a.bankbalance=-100
a.bankbalance=1000
print(a.bankbalance)
a.deposit(109)
# a.deposit(-90)
print(a.bankbalance)
a.withdraw(9)
print(a.bankbalance)