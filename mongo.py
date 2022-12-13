class AxisBank:
    branch = "chennai"
    pincode = 600094

class Customer(AxisBank):
    def __init__(self,firstname,lastname,accountno,balance):
        self.lname = firstname
        self.fname = lastname
        self.acno = accountno
        self.bal = balance

    def details(self):
        print(f"branch name:{self.branch}")
        print(f"pincode:{self.pincode}")
        print(f"lastname:{self.lname}")
        print(f"firstname:{self.fname}")
        print(f"account number:{self.acno}")
    
    def select(self):
        select = input("if you enter w or d:")
        if select == "w":
           print(self.withdraw())
        else:
            print(self.deposite())
    def deposite(self):
        amt = int(input("enter your deposite amount: "))
        self.bal += amt 
        print(f"{self.fname} your curent balance is:{self.bal}")
    
    def withdraw(self):
        amt = int(input("enter your withdraw amount: "))
        if self.bal >= amt:
            self.bal -= amt
            print("withdraw successfully")
            print(f"{self.fname} your current balance is:{self.bal}")
        else:
            print("insuffient balance")


modi = Customer("Modi","kesav",1555123,5000)
modi.details()
modi.select()