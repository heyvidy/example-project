"""
(c) 2018 - Speckbit Exploratories

Authors:
	Vidyadhar Sharma <vidyadhar@speckbit.com>

"""

class Account(object):
	"""
	General Account Class for a Bank Account

	Methods:
	withdraw(amount) -- withdraws the amount passed (default 0.0)
	deposit(amount) -- deposits a given amount to the balance
	check_balance -- returns the current account balance with name
	"""

	def __init__(self, account_name, opening_balance):
		"""
		Constructor function for the Account Class

		Attributes:
		self.name -- name of the account holder (str)
		self.balance -- the amount of cash in account (float) 
						is initialised with opening_balance when
						account is created.
		self.is_active -- The current status of the account
						  Checked while allowing transactions.
		"""

		self.name = account_name
		self.balance = opening_balance
		self.is_active = True



		