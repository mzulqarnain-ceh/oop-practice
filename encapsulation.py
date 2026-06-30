# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance #private Variable
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance+=amount
#             print(f"{amount} deposited. New Balance is: {self.__balance}")
#         else:
#             print("Enter a valid amount")
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Low balance please enter amount that is less than total balance")
#         else:
#             self.__balance-=amount
#             print(f"{amount} wihtdraw successfully! Remaining Balance is: {self.__balance}")
#     def get_balance(self):
#         return self.__balance
# acc=BankAccount("Ali",1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc.get_balance())
# try:
#     print(acc.__balance)
# except Exception as e:
#     print(e)

class Wallet:
    def __init__(self,owner,pin,balance):
        self.owner=owner
        self.__pin=pin
        self.__balance=balance
    def check_balance(self,pin):
        if pin==self.__pin:
            print(f"Your current balance is: {self.__balance}")
        else:
            print("Wrong Pin! please try again")
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited successfully! Your new balace is: {self.__balance}")
        else:
            print("Please enter a valid amount")
    def withdraw(self,pin,amount):
        if pin==self.__pin:
            if amount > self.__balance:
                print(f"Low Balance Please enter amount that is less than: {self.__balance}")
            elif amount<=0:
                print("Please enter a amount that is greater than 0")
            else:
                self.__balance-=amount
                print(f"{amount} withdraw successfully! Remaining balance is: {self.__balance}")
        else:
            print("Wrong Pin! Please enter a correct pin")
w=Wallet("ali", 9064, 1000)
# p=int(input("Enter your pin: "))
# w.check_balance(p)
w.check_balance(9064)
# w.check_balance(964)
w.deposit(1000)
# w.withdraw(9064,3000)
# w.withdraw(9064,-500)
w.withdraw(9064,500)
