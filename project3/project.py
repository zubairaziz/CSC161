def open_file(filename):
    try:
        file = open(filename, 'r')
        return file
    except FileNotFoundError as error:
        print(error)
        exit()


def parse_data(file):
    data = []
    for lines in file.readlines():
        line = lines.strip().split(',')
        data.append(line)
    return data


def get_values(filename, col):
    values = []
    file = open_file(filename)
    data = parse_data(file)
    del data[0]
    for i in range(len(data)):
        values.append(float(data[i][col]))
    return values


def test_data(filename, col, day):
    """A test function to query the data you loaded into your program.

    Args:
        filename: A string for the filename containing the stock data,
                  in CSV format.

        col: A string of either "date", "open", "high", "low", "close",
             "volume", or "adj_close" for the column of stock market data to
             look into.

             The string arguments MUST be LOWERCASE!

        day: An integer reflecting the absolute number of the day in the
             data to look up, e.g. day 1, 15, or 1200 is row 1, 15, or 1200
             in the file.

    Returns:
        A value selected for the stock on some particular day, in some
        column col. The returned value *must* be of the appropriate type,
        such as float, int or str.
    """
    cols = ["date", "open", "high", "low", "close", "volume", "adj_close"]
    file = open_file(filename)
    data = parse_data(file)
    for i in range(len(cols)):
        if (cols[i] == col):
            colNum = i
    val = data[day][colNum]
    file.close()
    return val


def transact(funds, stocks, qty, price, buy=False, sell=False):
    """A bookkeeping function to help make stock transactions.

       Args:
           funds: An account balance, a float; it is a value of how much money
                  you have, currently.

           stocks: An int, representing the number of stock you currently own.

           qty: An int, representing how many stock you wish to buy or sell.

           price: An float reflecting a price of a single stock.

           buy: This option parameter, if set to true, will initiate a buy.

           sell: This option parameter, if set to true, will initiate a sell.

       Returns:
           Two values *must* be returned. The first (a float) is the new
           account balance (funds) as the transaction is completed. The second
           is the number of stock now owned (an int) after the transaction is
           complete.

           Error condition #1: If the `buy` and `sell` keyword parameters are
           both set to true, or both false. You *must* print an error message,
           and then return the `funds` and `stocks` parameters unaltered. This
           is an ambiguous transaction request!

           Error condition #2: If you buy, or sell without enough funds or
           stocks to sell, respectively.  You *must* print an error message,
           and then return the `funds` and `stocks` parameters unaltered. This
           is an ambiguous transaction request!
    """
    qty = int(qty)
    price = float(price)
    total = price*qty
    if (buy):
        if (sell):
            # print(
            #     "Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
            return funds, stocks
        elif (funds < total):
            # print("Insufficient funds: purchase of {0} at ${1:.2f} requires {2:.5f}, but ${3:.2f} available!".format(
            #     qty, price, total, funds))
            return funds, stocks
        else:
            stocks_owned = stocks + qty
            cash_balance = funds - total
            return cash_balance, stocks_owned
    elif (sell):
        if (stocks < qty):
            # print('Insufficient stock: {0} stocks owned, but selling {1}!'.format(
            #     stocks, qty))
            return funds, stocks
        else:
            stocks_owned = stocks - qty
            cash_balance = funds + total
            return cash_balance, stocks_owned
    else:
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
        return funds, stocks


def alg_moving_average(filename):
    """This function implements the moving average stock trading algorithm.

    The CSV stock data should be loaded into your program; use that data to
    make decisions using the moving average algorithm.

    Any bookkeeping setup from Milestone I should be called/used here.

    Algorithm:
    - Trading must start on day 21, taking the average of the previous 20 days.
    - You must buy shares if the current day price is 5%, or more, lower than
      the moving average.
    - You must sell shares if the current day price is 5% higher, or more than
      the moving average.
    - You must buy, or sell 10 stocks per transaction.
    - You are free to choose which column of stock data to use (open, close,
      low, high, etc)

    Args:
        A filename, as a string.

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """

    # Last thing to do, return two values: one for the number of stocks you
    # end up owning after the simulation, and the amount of money you have
    # after the simulation.
    # Remember, all your stocks should be sold at the end!
    stocks_owned = 0
    cash_balance = 1000
    qty = 0
    current_average = 0
    open_values = get_values(filename, 1)
    for i in range(len(open_values)):
        if (i >= 19):
            current_average = sum(open_values[i-19:i])/20
            current_price = open_values[i]
            if (current_average <= (0.95*current_price)):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, 10, current_price, True, False)
            elif ((current_average >= (1.05*current_price)) and
                    (stocks_owned >= 10)):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, 10, current_price, False, True)
        if (i == (len(open_values)-1)):
            cash_balance, stocks_owned = transact(
                cash_balance, stocks_owned, stocks_owned, current_price,
                False, True)
    return stocks_owned, cash_balance


def alg_mine(filename):
    """This function implements the student's custom trading algorithm.

    Using the CSV stock data that should be loaded into your program, use
    that data to make decisions using your own custome trading algorithm.

    Also, any bookkeeping setup in Milestone I should be called/used here.

    Args:
        A filename, as a string.

    Algorithm:
    [REPLACE THIS WITH A CLEAR DESCRIPTION OF YOUR ALGORITHM]

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """

    # Last thing to do, return two values: one for the number of stocks you
    # end up owning after the simulation, and the amount of money you have
    # after the simulation.
    # Remember, all your stocks should be sold at the end!
    stocks_owned = 0
    cash_balance = 1000
    qty = 0
    historic_high = 0
    historic_low = 1000  # arbitrary number that is really high
    high_values = get_values(filename, 2)
    low_values = get_values(filename, 3)
    for i in range(len(high_values)):
        low_price = low_values[i]
        high_price = high_values[i]
        to_buy = (cash_balance//low_price)
        if (low_price < historic_low):
            historic_low = low_price
        if (high_price > historic_high):
            historic_high = high_price
        if (i >= 99):
            if (high_price == historic_high):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, stocks_owned, high_price,
                    False, True)
            if (low_price == historic_low):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, to_buy, high_price,
                    True, False)
        if (i >= 4):
            five_day_average_low = sum(low_values[i-4:i])/5
            five_day_average_high = sum(low_values[i-4:i])/5
        if (i >= 19):
            twenty_day_average_low = sum(high_values[i-19:i])/19
            twenty_day_average_high = sum(high_values[i-19:i])/19
            # Start trading at day 21
            if (five_day_average_low <= (0.95*twenty_day_average_low)):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, to_buy, low_price, True, False)
            elif ((five_day_average_high >= (1.2*twenty_day_average_high)) and
                    (stocks_owned >= 10)):
                cash_balance, stocks_owned = transact(
                    cash_balance, stocks_owned, 10, high_price, False, True)
        if (i == (len(high_values)-1)):
            cash_balance, stocks_owned = transact(
                cash_balance, stocks_owned, stocks_owned, high_price,
                False, True)
    return stocks_owned, cash_balance


def main():
    # My testing will use AAPL.csv or MSFT.csv
    filename = input("Enter a filename for stock data (CSV format): ")

    # Call your moving average algorithm, with the filename to open.
    alg1_stocks, alg1_balance = alg_moving_average(filename)

    # Print results of the moving average algorithm, returned above:
    print("The results are...\nStocks owned: {0}, Cash balance: {1:.2f}".format(
        alg1_stocks, alg1_balance))

    # Now, call your custom algorithm!
    alg2_stocks, alg2_balance = alg_mine(filename)

    # Print results of your algorithm, returned above:
    print("The results are...\nStocks owned: {0}, Cash balance: {1:.2f}".format(
        alg2_stocks, alg2_balance))


if __name__ == '__main__':
    main()
