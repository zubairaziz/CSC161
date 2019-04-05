from account import Account

# Storing accounts locally since we're not using a database
my_accounts = [
    {'first_name': 'Zubair', 'last_name': 'Aziz',
        'PIN': 1234, 'balance': 1000.00},
    {'first_name': 'Chase', 'last_name': 'Lindemann',
        'PIN': 1234, 'balance': 1234.00},
    {'first_name': 'Sam', 'last_name': 'Schacht',
        'PIN': 1234, 'balance': 512.00},
    {'first_name': 'Ian', 'last_name': 'Lawson',
        'PIN': 1234, 'balance': 585.00},
    {'first_name': 'Ashley', 'last_name': 'Lin',
        'PIN': 1234, 'balance': 811.00},
]


class ATM:
    def __init__(self):
        self.accounts = self.generateAccounts(my_accounts)
        self.authenticated = False
        # self.currentUser = None

    def generateAccounts(self, account_list):
        accounts = []
        for i in range(len(account_list)):
            accounts.append(Account(account_list[i]['first_name'],
                                    account_list[i]['last_name'],
                                    account_list[i]['PIN'],
                                    account_list[i]['balance']))
        return accounts

    def menu(self):
        print('Welcome to pyBank\n')
        if (not self.authenticated):
            self.doLogin()
            self.menu()
        else:
            print('Welcome {0}\n'.format(self.currentUser.first_name))
            print('What would you like to do? (Pick a number)')
            print('\t1. Check balance')
            print('\t2. Deposit cash')
            print('\t3. Withdraw cash')
            print('\t4. Logout')
            choice = int(input('Answer: '))
            if (choice == 1):
                print('Account Balance: ${0:.2f}'.format(
                    self.currentUser.balance))
                self.menu()
            elif (choice == 2):
                self.doDeposit()
            elif (choice == 3):
                self.doWithdraw()
            elif (choice == 4):
                print('Thank you for using pyBank')
                self.logout()

    def loginUser(self, PIN):
        currentUser = self.currentUser
        authenticated = currentUser.confirmPIN(PIN)
        return authenticated

    def getAccount(self, userID):
        for i in self.accounts:
            if i.userID == userID:
                currentUser = i
        return currentUser

    def doLogin(self):
        print('Login')
        userID = input('Enter User ID: ')
        PIN = int(input('Enter PIN: '))
        self.currentUser = self.getAccount(userID)
        self.authenticated = self.loginUser(PIN)

    def doDeposit(self):
        print('Deposit')
        amount = float(
            input('How much cash would you like to deposit? '))
        self.currentUser.deposit(amount)
        print('New Balance: ${0:.2f}'.format(
            self.currentUser.balance))
        self.menu()

    def doWithdraw(self):
        print('Withdraw')
        amount = int(
            input('How much cash would you like to withdraw? '))
        self.currentUser.withdraw(amount)
        print('New Balance: ${0:.2f}'.format(
            self.currentUser.balance))
        self.menu()

    def logout(self):
        self.authenticated = False
        self.currentUser = None
        self.menu()

    def __repr__(self):
        for i in self.accounts:
            print(i)
        return ""
