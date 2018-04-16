#!/usr/bin/env python3
"""
Chapter 15 - Classes
@author Ellery Penas
@version 2018.04.16
"""


class Account:
    """This class maintains data and functions for interacting with a
    bank account balance.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    def __init__(self, filepath):
        Account.__init__(self, filepath)


def main():
    """test init of function"""
#    account = Account(
#        '/projects/eejay73-python-class-app/CH15-classes/balance.txt')
#    print(account)
#    print(account.balance)
#    print('Withdraw 100...')
#    account.withdraw(100)
#    print(account.balance)
#    account.commit()

    checking = Checking(
        '/projects/eejay73-python-class-app/CH15-classes/balance.txt')
    checking.deposit(10)
    print(checking.balance)


if __name__ == "__main__":
    main()
