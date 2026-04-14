#type: ignore
class account:
    def __init__(self, id, holdername):
        self.id=id
        self.holdername=holdername
        self._balance=0
    def check_balance(self):
        print(f"balance:{self._balance}")
    def deposit(self, amount):
        self._balance +=amount
        print(f"amount deposited successfully. updated balance:{self._balance}")
    def withdraw(self, amount):
        if self._balance>=amount:
            self._balance -=amount
            print(f"amount withdrawl successfull. updated balance:{self._balance}")
        else:
            print("insufficient balance")
class saving_account(account):
    def calculate_interest(self):
        interest_rate=0.04
        interest=self._balance*interest_rate
        print(f"interest: {interest}")
class current_account(account):
    def withdraw(self, amount):
        overdraft_limit = 1000
        if self._balance +overdraft_limit >=amount:
            self._balance -=amount
            print(f"withdraw successful. update balance:{self._balance}")
        else:
            print("insufficient balance")

class bank:
    def __init__(self, name, city):  
        self.name=name
        self.city=city
        self._accounts={}
    def create_account(self, id, holdername, type):
        if type=="saving":
            new_account=saving_account(id, holdername)
        elif type=="current":
            new_account=current_account(id, holdername)
        self._accounts[id]=new_account
        print("account creation successfully completed")
        return new_account
    def get_account(self, id):
        if id  not in self._accounts:
            print("account not found")
            return None
        else:
            self._accounts[id]
            print(f"id:{self._accounts.id} /n holdername:{self._accounts.holdername}")
            return self._accounts
        
pbi=bank("pramod bank of india", "haveri")
print("--------------------PRAMOD BANK OF INDIA--------------------------")
s1=pbi.create_account("1", "vijay", "saving")
c1=pbi.create_account("2", "raju", "current")
s1.deposit(1000)
c1.deposit(50)
s1.withdraw(500)
c1.withdraw(99)
s1.calculate_interest()