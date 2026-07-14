# price=int(input("Enter the price of Car: "))
# down_payment=int(input("Enter the down payment: "))
# if down_payment>=price:
#     print(f"The down payment must be less than {price}")
#     exit()
# interest_rate=float(input("Enter the interest rate: "))
# duration=int(input("Enter the duration of loan in years: "))
# n=duration*12
# loan_amount=price-down_payment
# monthly_interest=interest_rate/12/100
# emi=loan_amount * monthly_interest * (1+monthly_interest)**n / ((1+monthly_interest)**n-1)
# print(f"The loan amount is: {loan_amount:,.2f} \n")
# print(f"The EMI is: {emi:,.2f}")
# total_amount=emi*duration*12
# print(f"The total amount you will pay {total_amount:,.2f}")
# total_interest=total_amount-loan_amount
# print(f"The total interest you will pay {total_interest:,.2f}")
# total_cost=total_amount+down_payment
# print(f"The total cost of car with interest is {total_cost:,.2f}")

# 🏠 Simple Interest & Compound Interest Calculator with Investment Growth
principal_amount=int(input("Enter pricipal amount: "))
interest_rate=float(input("Enter the interest rate: "))
time=int(input("Enter the duration in years: "))
if principal_amount<=0 or interest_rate<=0 or time<=0:
    print("All values must b positive")
    exit()
choice=input("Ener choice for simple interest: s and for compound interest a: ").lower()
if choice=="s":
    total_interest_si= (principal_amount * interest_rate * time)/100
    print(f"The total interest with simple interest is: {total_interest_si:,.2f}")
    total_amount=principal_amount + total_interest_si
    print(f"The total amount with simple interest is: {total_amount:,.2f}")
    maturity_value=total_amount
    print(f"Maturity value with simple interest: {maturity_value:,.2f}")
elif choice=="a":
    maturity_value = principal_amount * (1 + interest_rate/100)**time
    print(f"Maturity value with compound interest: {maturity_value:,.2f}")
    total_amount=maturity_value
    print(f"Total amount with compound interest: {total_amount:,.2f}")
    total_interest=maturity_value-principal_amount
    print(f"Total interest with compound interest is: {total_interest:,.2f}")
else:
    print("Please choose a valid choice s or a")
    exit()
