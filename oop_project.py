from bank import *

Sivanesh = BankAccount(10000, "Sivanesh")
Sharanya = BankAccount(1000, "Sharanya")

Sivanesh.get_balance()

Sivanesh.deposit(500)
Sharanya.deposit(300)

Sivanesh.withdrawl(5000)
Sharanya.transfer(300,Sivanesh)

Mani = InterestRewards(100,"Mani")
Mani.get_balance()
Mani.deposit(100)

Kani = SavingsAccount(1000,"Kani")
Kani.get_balance()
Kani.withdrawl(100)
Kani.transfer(5,Sharanya)