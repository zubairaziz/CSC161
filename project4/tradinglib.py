from filehandler import Filehandler


class TradingLibrary:

    def __init__(self):
        self.cash_balance = 0
        self.stocks_owned = 0
        self.historic_high = 0
        self.historic_low = 0
        self.total_bought = 0
        self.file = Filehandler()
        self.stock_data = self.file.data
        self.open_values = self.get_values(1)
        self.close_values = self.get_values(4)
        self.low_values = self.get_values(3)
        self.high_values = self.get_values(2)

    def get_values(self, col):
        values = []
        data = self.stock_data
        del data[0]
        for i in range(len(data)):
            values.append(float(data[i][col]))
        return values

    def transact(self, qty, price, buy=False, sell=False):
        qty = int(qty)
        price = float(price)
        total = price*qty
        if (buy):
            if (sell):
                # print(
                #     "Ambigious transaction! Can't determine whether to buy
                # or sell. No action performed.")
                pass
            elif (self.cash_balance < total):
                # print("Insufficient funds: purchase of {0} at ${1:.2f}
                # requires {2:.5f}, but ${3:.2f} available!".format(
                #     qty, price, total, funds))
                pass
            else:
                self.stocks_owned = self.stocks_owned + qty
                self.cash_balance = self.cash_balance - total
                self.total_bought = self.total_bought + qty
        elif (sell):
            if (self.stocks_owned < qty):
                # print('Insufficient stock: {0} stocks owned, but selling \
                # {1}!'.format(stocks, qty))
                pass
            else:
                self.stocks_owned = self.stocks_owned - qty
                self.cash_balance = self.cash_balance + total
        else:
            print(
                "Ambigious transaction! Can't determine whether to buy or sell. \
                    No action performed.")

    def alg_moving_average(self):
        self.cash_balance = 1000.00
        self.stocks_owned = 0
        self.historic_high = 0
        self.historic_low = 1000
        self.total_bought = 0
        print('alg_moving_average() called on {0}'.format(self.file))
        qty = 0
        current_average = 0
        open_values = self.open_values
        for i in range(len(open_values)):
            if (open_values[i] < self.historic_low):
                self.historic_low = open_values[i]
            if (open_values[i] > self.historic_high):
                self.historic_high = open_values[i]
            if (i >= 19):
                current_average = sum(open_values[i-19:i])/20
                current_price = open_values[i]
                if (current_average <= (0.95*current_price)):
                    self.transact(10, current_price, True, False)
                elif ((current_average >= (1.05*current_price)) and
                        (self.stocks_owned >= 10)):
                    self.transact(10, current_price, False, True)
            if (i == (len(open_values)-1)):
                self.transact(self.stocks_owned, current_price, False, True)

    def alg_mine(self):
        self.cash_balance = 1000.00
        self.stocks_owned = 0
        self.historic_high = 0
        self.historic_low = 1000
        self.total_bought = 0
        print('alg_mine() called on "{0}"'.format(self.file))
        high_values = self.high_values
        low_values = self.low_values
        qty = 0
        for i in range(len(high_values)):
            low_price = low_values[i]
            high_price = high_values[i]
            to_buy = (self.cash_balance//low_price)
            if (low_price < self.historic_low):
                self.historic_low = low_price
            if (high_price > self.historic_high):
                self.historic_high = high_price
            if (i >= 99):
                if (high_price == self.historic_high):
                    self.transact(
                        self.stocks_owned, high_price,
                        False, True)
                if (low_price == self.historic_low):
                    self.transact(
                        to_buy, high_price,
                        True, False)
            if (i >= 4):
                five_day_average_low = sum(low_values[i-4:i])/5
                five_day_average_high = sum(low_values[i-4:i])/5
            if (i >= 19):
                twenty_day_average_low = sum(high_values[i-19:i])/19
                twenty_day_average_high = sum(high_values[i-19:i])/19
                # Start trading at day 21
                if (five_day_average_low <= (0.95*twenty_day_average_low)):
                    self.transact(to_buy, low_price, True, False)
                elif ((five_day_average_high >=
                        (1.2*twenty_day_average_high)) and
                        (self.stocks_owned >= 10)):
                    self.transact(10, high_price, False, True)
            if (i == (len(high_values)-1)):
                self.transact(self.stocks_owned, high_price, False, True)

    def __repr__(self):
        return"Stocks owned: {0}\nCash Balance: ${1:.2f}".format(
            self.stocks_owned, self.cash_balance)
