#Create a Budget class that can instantiate objects based on different budget categories
# E.g. food, clothing, and entertainment. 
# Allow for depositing and withdrawing funds from each category
# Include computing category balances and transferring balance amounts between categories


class budget:

    def __init__(self, balance=0,):
        self.balance = balance

    def balance_check(self):
        self.balance = int(input("How much is your balance? "))
        print(f"Your current balance is £{self.balance}")

    def balance_add(self, addval):
        self.balance = addval + self.balance


    def balance_remove(self, removeval):
        self.balance = self.balance - removeval

    def transfer(self, transferval, budget_name):
        self.balance_add(transferval)
        budget_name.balance_remove(transferval)


clothes = budget(50)
food = budget(100)
pets = budget (400)


food.balance_add(100)
print(f"This is your food balance: £{food.balance}")
clothes.balance_add(1000)
print(f"This is your clothes balance: £{clothes.balance}")
clothes.balance_remove(500)
print(f"This is your clothes balance: £{clothes.balance}")
clothes.transfer(500, food)
pets.transfer(300, food)
print(f"This is your pets balance: £{pets.balance}")
print(f"This is your clothes balance: £{clothes.balance}")
print(f"This is your food balance: £{food.balance}")