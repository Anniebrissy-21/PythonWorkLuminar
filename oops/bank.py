from datetime import datetime

class Bank:
    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.bank_name} has been credited with {amount} avl bal is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} avl balance is {self.balance}")

    def get_balance(self):
        print(f"Your {self.bank_name} A/C {self.acno} bal on {datetime.today()} is {self.balance}")
obj1=Bank()
obj1.create("sbi","10234","vijay","savings",4000)

obj1.get_balance()
obj1.deposit(4000)


obj2=Bank()
obj2.create("sbi","10236","jhon","savings",5000)

obj2.withdraw(3000)