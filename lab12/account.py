class Account:
    def __init__(self, first_name, last_name, PIN, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.userID = self.generateUserID()
        self.PIN = PIN
        self.balance = balance

    def generateUserID(self):
        # Generates a userID with the first letter of firstname and lastname
        userID = self.first_name[0].lower()+self.last_name.lower()
        return userID

    def confirmPIN(self, PIN):
        if (PIN == self.PIN):
            return True
        else:
            return False

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if (amount <= 0):
            print('Cannot deposit 0 or a negative number')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if (amount > self.balance):
            print('Cannot withdraw more cash than you have in your account')
        elif (amount <= 0):
            print('Cannot withdraw 0 or a negative number')
        else:
            self.balance -= amount

    def __repr__(self):
        return "First Name: {0}\nLast Name: {1}\nUser ID: {2}\nBalance: {3:.2f}\
            \n".format(self.first_name, self.last_name, self.userID,
                       self.balance)
