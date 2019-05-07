from account import Account
from time import sleep
from graphics import GraphWin, Circle, Point, Line, Rectangle, Text, Entry

# Storing accounts locally since we're not using a database
my_accounts = [
    {'first_name': 'Zubair', 'last_name': 'Aziz',
        'PIN': 1234, 'balance': 1000.00},
    {'first_name': 'Chase', 'last_name': 'Lindemann',
        'PIN': 1234, 'balance': 1234.00},
    {'first_name': 'Sam', 'last_name': 'Schacht',
        'PIN': 1234, 'balance': 812.00},
    {'first_name': 'Ian', 'last_name': 'Lawson',
        'PIN': 1234, 'balance': 885.00},
    {'first_name': 'Ashley', 'last_name': 'Lin',
        'PIN': 1234, 'balance': 811.00},
]

# Graphics Objects
screen = Rectangle(Point(100, 100), Point(700, 750))
screen.setFill('cyan')
heading = Text(Point(400, 50), "ATM")
heading.setSize(30)
# Hint
hintText = Text(Point(400, 700),
                "Try logging in with the userID `zaziz` and PIN `1234`\
                    \nother accounts inlude `alin`, `sschacht`, `ilawson`, `clindemann`\
                    \nPIN is `1234` for all accounts")
# Messages
errorMessage = Text(Point(400, 215), "Error")
errorMessage.setSize(18)
errorMessage.setTextColor('red')
message = Text(Point(400, 150), "Welcome to PyBank")
message.setSize(20)
message2 = Text(Point(400, 325), "Login")
message2.setSize(20)
message3 = Text(Point(400, 325), "What would you like to do?")
# User ID
uidText = Text(Point(400, 375), "User ID")
uidInput = Entry(Point(400, 400), 10)
# PIN
pinText = Text(Point(400, 425), "PIN")
pinInput = Entry(Point(400, 450), 4)
# Login
loginBtn = Rectangle(Point(375, 475), Point(425, 505))
loginBtn.setFill("green")
loginBtnText = Text(Point(400, 490), "Login")
# Deposit
depositBtn = Rectangle(Point(250, 375), Point(350, 405))
depositBtn.setFill("blue")
depositBtnText = Text(Point(300, 390), "Deposit")
# Withdraw
withdrawBtn = Rectangle(Point(450, 375), Point(550, 405))
withdrawBtn.setFill("blue")
withdrawBtnText = Text(Point(500, 390), "Withdraw")
# Balance
balanceBtn = Rectangle(Point(250, 575), Point(350, 605))
balanceBtn.setFill("blue")
balanceBtnText = Text(Point(300, 595), "Balance")
# Logout
logoutBtn = Rectangle(Point(450, 575), Point(550, 605))
logoutBtn.setFill("red")
logoutBtnText = Text(Point(500, 595), "Log Out")
# Amount
amountText = Text(Point(400, 375), "Amount")
amountInput = Entry(Point(400, 400), 10)
# Accept
acceptBtn = Rectangle(Point(375, 475), Point(425, 505))
acceptBtn.setFill("blue")
acceptBtnText = Text(Point(400, 490), "Accept")
# Back
backBtn = Rectangle(Point(375, 680), Point(425, 710))
backBtn.setFill("red")
backBtnText = Text(Point(400, 700), "Back")
# Back
quitBtn = Rectangle(Point(682, 102), Point(698, 118))
quitBtn.setFill("red")
quitBtnText = Text(Point(690, 110), "X")
quitBtnText.setTextColor("white")


def click(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)
    return ll.getX() < point.getX() < ur.getX() and ll.getY()\
        < point.getY() < ur.getY()


def undrawAll():
    # Undraws all components on the screen
    message.undraw()
    message2.undraw()
    uidText.undraw()
    uidInput.undraw()
    pinText.undraw()
    pinInput.undraw()
    loginBtn.undraw()
    loginBtnText.undraw()
    depositBtn.undraw()
    withdrawBtn.undraw()
    balanceBtn.undraw()
    logoutBtn.undraw()
    depositBtnText.undraw()
    withdrawBtnText.undraw()
    balanceBtnText.undraw()
    logoutBtnText.undraw()
    backBtn.undraw()
    backBtnText.undraw()
    acceptBtn.undraw()
    acceptBtnText.undraw()
    amountText.undraw()
    amountInput.undraw()
    hintText.undraw()


def drawLoginScreen(target):
    # Draws screen components for login screen
    undrawAll()
    message.setText("Welcome to PyBank")
    message.draw(target)
    message2.setText('Login')
    message2.draw(target)
    uidText.draw(target)
    uidInput.draw(target)
    pinText.draw(target)
    pinInput.draw(target)
    loginBtn.draw(target)
    loginBtnText.draw(target)
    hintText.draw(target)


def drawMainMenu(target, displayName):
    # Draws screen components for main menu
    undrawAll()
    message.setText("Welcome to PyBank, {0}".format(displayName))
    message.setSize(30)
    message.draw(target)
    message2.setText("What would you like to do?")
    message2.draw(target)
    depositBtn.draw(target)
    withdrawBtn.draw(target)
    balanceBtn.draw(target)
    logoutBtn.draw(target)
    depositBtnText.draw(target)
    withdrawBtnText.draw(target)
    balanceBtnText.draw(target)
    logoutBtnText.draw(target)


def drawBalanceScreen(target, amount):
    # Draws screen components for balance screen
    undrawAll()
    message2.setText('Account Balance: ${0:.2f}'.format(amount))
    message2.draw(target)
    backBtn.draw(target)
    backBtnText.draw(target)


def drawDepositScreen(target):
    # Draws screen components for deposit screen
    undrawAll()
    message2.setText('Deposit')
    message2.draw(target)
    amountText.draw(target)
    amountInput.draw(target)
    acceptBtn.draw(target)
    acceptBtnText.draw(target)
    backBtn.draw(target)
    backBtnText.draw(target)


def drawWithdrawScreen(target):
    # Draws screen components for withdraw screen
    undrawAll()
    message2.setText('Withdraw')
    message2.draw(target)
    amountText.draw(target)
    amountInput.draw(target)
    acceptBtn.draw(target)
    acceptBtnText.draw(target)
    backBtn.draw(target)
    backBtnText.draw(target)


def showError(target, message, color='red'):
    # Shows errors and alerts
    errorMessage.setText(message)
    errorMessage.setTextColor(color)
    errorMessage.draw(target)
    sleep(1.5)
    errorMessage.undraw()


def quit(target, items):
    # Exit with `X` button
    for item in items[:]:
        item.undraw()
    exit()


class ATM:

    def __init__(self):
        # Initialize atm
        self.accounts = self.setAccounts(my_accounts)
        self.authenticated = False
        self.currentUser = None
        self.win = GraphWin('Python ATM', 800, 800)
        self.win.setBackground('gray')
        # Graphics Headings
        heading.draw(self.win)
        screen.draw(self.win)
        hintText.draw(self.win)
        quitBtn.draw(self.win)
        quitBtnText.draw(self.win)

    def setAccounts(self, account_list):
        accounts = []
        for i in range(len(account_list)):
            accounts.append(Account(account_list[i]['first_name'],
                                    account_list[i]['last_name'],
                                    account_list[i]['PIN'],
                                    account_list[i]['balance']))
        return accounts

    def setCurrentUser(self, userID):
        for user in self.accounts:
            if (user.userID == userID):
                self.currentUser = user

    def setAuthenticated(self, PIN):
        self.authenticated = self.currentUser.confirmPIN(PIN)

    def doLogin(self):
        # Draw login GUI
        drawLoginScreen(self.win)
        while (self.authenticated is False):
            clickPoint = self.win.getMouse()
            if clickPoint is None:
                pass
            elif click(clickPoint, loginBtn):
                try:
                    userID = uidInput.getText()
                    PIN = int(pinInput.getText())
                    self.setCurrentUser(userID)
                    if (self.currentUser is not None):
                        self.setAuthenticated(PIN)
                        if (not self.authenticated):
                            showError(self.win, "Error: Incorrect PIN")
                            self.currentUser = None
                    else:
                        showError(self.win, "Error: User not found")
                except ValueError as error:
                    showError(self.win, "Value Error: see console for details")
                    print(error)
            elif click(clickPoint, quitBtn):
                quit(self.win, self.win.items)
            else:
                pass

    def doDeposit(self):
        drawDepositScreen(self.win)
        showError(self.win, 'Balance: ${0:.2f}'.format(
            self.currentUser.balance), 'green')
        while (self.authenticated):
            clickPoint = self.win.getMouse()
            if clickPoint is None:
                pass
            elif click(clickPoint, acceptBtn):
                try:
                    amount = float(amountInput.getText())
                    self.currentUser.deposit(amount)
                    if (amount <= 0):
                        showError(
                            self.win, 'Amount cannot be less than or equal to 0')
                    else:
                        showError(self.win, 'New Balance: ${0:.2f}'.format(
                            self.currentUser.balance), 'green')
                except ValueError as error:
                    showError(self.win, "Value Error: see console for details")
                    print(error)
            elif click(clickPoint, backBtn):
                self.menu()
            elif click(clickPoint, quitBtn):
                quit(self.win, self.win.items)
            else:
                pass

    def doWithdraw(self):
        drawWithdrawScreen(self.win,)
        showError(self.win, 'Balance: ${0:.2f}'.format(
            self.currentUser.balance), 'green')
        while (self.authenticated):
            clickPoint = self.win.getMouse()
            if clickPoint is None:
                pass
            elif click(clickPoint, acceptBtn):
                try:
                    amount = float(amountInput.getText())
                    self.currentUser.withdraw(amount)
                    if (amount >= self.currentUser.balance):
                        showError(
                            self.win, 'Cannot withdraw more than your balance')
                    else:
                        showError(self.win, 'New Balance: ${0:.2f}'.format(
                            self.currentUser.balance), 'green')
                except ValueError as error:
                    showError(self.win, "Value Error: see console for details")
                    print(error)
            elif click(clickPoint, backBtn):
                self.menu()
            elif click(clickPoint, quitBtn):
                quit(self.win, self.win.items)
            else:
                pass

    def logout(self):
        self.authenticated = False
        self.currentUser = None
        self.menu()

    def __repr__(self):
        for account in self.accounts:
            print(account)
        return ""

    def menu(self):
        if (not self.authenticated):
            self.doLogin()
            self.menu()
        else:
            drawMainMenu(self.win, self.currentUser.first_name)
            while(self.authenticated):
                clickPoint = self.win.getMouse()
                if clickPoint is None:
                    pass
                elif click(clickPoint, balanceBtn):
                    drawBalanceScreen(self.win, self.currentUser.balance)
                    while(self.authenticated):
                        clickPoint = self.win.getMouse()
                        if clickPoint is None:
                            pass
                        elif click(clickPoint, backBtn):
                            self.menu()
                        elif click(clickPoint, quitBtn):
                            quit(self.win, self.win.items)
                        else:
                            pass
                elif click(clickPoint, depositBtn):
                    self.doDeposit()
                elif click(clickPoint, withdrawBtn):
                    self.doWithdraw()
                elif click(clickPoint, logoutBtn):
                    undrawAll()
                    showError(self.win, 'Thank you for using PyBank', 'blue')
                    self.logout()
                elif click(clickPoint, quitBtn):
                    quit(self.win, self.win.items)
                else:
                    pass
