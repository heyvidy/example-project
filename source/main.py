from bank import AccountManager
from tabulate import tabulate

accounts = {}
account_no = 8400 
print(" -"*20, "\nWelcome to Speckbit International Bank\n","- "*20)

while True:
	print("\n\n")	
	print("How can we help you today?\n\nFeel free to choose from the following options.\n")
	print(tabulate([(1, "Withdraw",), (2, "Deposit",), (3, "Statement",), (4, "Create Account",)], tablefmt="fancy_grid"))
	
	# Taking the user's choice from options
	ch = int(input("\nPlease enter an option: "))

	if ch == 1:
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")
		if upin == accounts[acc_no].pin:
			amt = float(input("Enter Amount: "))
			accounts[acc_no].withdraw(amt)
	elif ch == 2:
		#Perform deposit
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")
		if upin == accounts[acc_no].pin:
			amt = float(input("Enter Amount: "))
			accounts[acc_no].deposit(amt)

	elif ch == 3:
		# Return statment of account
		acc_no = input("Enter account no: ")
		upin = input("Enter pin: ")
		if upin == accounts[acc_no].pin:
			statement = accounts[acc_no].acc_statement()
			print(statement)

	elif ch == 4:
		name = input("Enter Name: ")
		balance = eval(input("Enter Opening Balance: "))
		pin = input("Create a 4 digit pin for your account: ")
		accounts[str(account_no)] = AccountManager(account_no, name, balance, pin)
		print("Account Created Successfully! You account no is {}".format(account_no))
		account_no += 1
	else:
		break
