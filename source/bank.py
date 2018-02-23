"""
Bank Management Module

Authors:
	Vidyadhar Sharma <vidyadhar@speckbit.com>
"""

from tabulate import tabulate

class AccountManager(object):
	"""
	General Account Class for a Bank Account

	check_balance -- returns the current account balance with name
	"""

	def __init__(self, account_no, account_name, opening_balance, pin):
		"""
		Constructor function for the Account Class
		Executed by interpreter to create an instance of this class.

		Attributes:
			self.name -- name of the account holder (str)

			self.balance -- the amount of cash in account (float) 
			self.is_active -- The current status of the account
		"""

		self.name = account_name
		self.account_no = account_no
		self.balance = float(opening_balance)
		self.is_active = True
		self.transactions = []
		self.pin = pin


	def withdraw(self, amount=0.0):
		"""
		withdraws the amount passed
		params:
		amount - the amount to be withdrawn from balance (float)
		"""
		if (self.balance - amount) < 0:
			print("Insufficient balance. Please try a smaller amount.")
		else:
			self.balance -= float(amount)

			# Log the transaction in transaction history
			transaction = ("-"+str(amount), self.balance)
			self.transactions.append(transaction)


	def deposit(self, amount=0.0):
		"""
		deposits a given amount to the balance.

		params:
		amount - the amount to be deposited (float) (default 0.0)
		"""
		self.balance += amount

		# Log the transaction on transaction history
		transaction = ("+"+str(amount), self.balance)
		self.transactions.append(transaction)		


	def acc_statement(self):
		"""
		returns the statement of account for the account
		"""
		if self.is_active:
			status = "Active"
		else:
			status = "Blocked"

		statement = tabulate(self.transactions, tablefmt="fancy_grid", headers=["Transactions", "Remaining Bal"])

		return statement
