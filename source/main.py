"""
Bank Management Application Script

Authors:
	Vidyadhar Sharma <vidyadhar@speckbit.com>
"""

from bank import AccountManager
from tabulate import tabulate

"""
**Variables**
	
	accounts: (dict) {account_no: Account Manager Object} 
			  holds all the accounts created during the session.
	account_no: (int) - Set to 8400 by default, account no. allocation starts here. 
				Incremented after every new account creation
"""

accounts = {}
account_no = 8400 
print(" -"*20, "\nWelcome to Speckbit International Bank\n","- "*20)

# Application Loop
while True:

	print("\n\n")	
	print("How can we help you today?\n\nFeel free to choose from the following options.\n")

	# Print the options in a table
	print(tabulate([(1, "Withdraw",), (2, "Deposit",), (3, "Statement",), (4, "Create Account",)], tablefmt="fancy_grid"))
	
	# Taking the user's choice from options as (int)
	ch = int(input("\nPlease enter an option: "))

	"""
	If user choice is 1 (int) - perform withdrawal operation
	"""
	if ch == 1:


		# Get User Account Details
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")


		if upin == accounts[acc_no].pin:
			amt = float(input("Enter Amount: "))

			# Withdraw the specified amount from the respective account
			accounts[acc_no].withdraw(amt)


	"""
	If user choice is 2 (int) - perform deposit operation
	"""
	elif ch == 2:
		#Perform deposit

		# Get User Account Details
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")

		if upin == accounts[acc_no].pin:
			amt = float(input("Enter Amount: "))

			#Deposit the amount to the account object
			accounts[acc_no].deposit(amt)

	"""
	If user choice is 3 (int) - perform get statement operation
	"""
	elif ch == 3:

		# Get User Account Details
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")

		if upin == accounts[acc_no].pin:

			#Fetch statement from object
			statement = accounts[acc_no].acc_statement()

			# Return statment of account
			print(statement)

	"""
	If user choice is 4 (int) - Create new account with info
	"""
	elif ch == 4:

		# Ask for basic info needed to create an account
		name = input("Enter Name: ")
		balance = eval(input("Enter Opening Balance: "))
		pin = input("Create a 4 digit pin for your account: ")

		# Use the current account_no count to assign an account no and save the object
		accounts[str(account_no)] = AccountManager(account_no, name, balance, pin)
		print("Account Created Successfully! You account no is {}".format(account_no))
		
		# Increment the count after successful creation of account
		account_no += 1

	else:

		# Exit the loop if input is invalid.
		break
