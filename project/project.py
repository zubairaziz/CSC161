def open_file(filename):
    try:
        file = open(filename, 'r')
        return file
    except FileNotFoundError as error:
        print(error)
        exit()


def parse_data(file):
    data = []
    for line in file:
        line = line.strip().split(',')
        data.append(line)
    return data


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
            print(
                "Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
            return funds, stocks
        elif (funds < total):
            print("Insufficient funds: purchase of {0} at ${1:.2f} requires {2:.5f}, but ${3:.2f} available!".format(
                qty, price, total, funds))
            return funds, stocks
        else:
            stocks_owned = stocks + qty
            cash_balance = funds - total
            return cash_balance, stocks_owned
    elif (sell):
        if (stocks < qty):
            print('Insufficient stock: {0} stocks owned, but selling {1}!'.format(
                stocks, qty))
            return funds, stocks
        else:
            stocks_owned = stocks - qty
            cash_balance = funds + total
            return cash_balance, stocks_owned
    else:
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
        return funds, stocks


def main():
    pass


if __name__ == '__main__':
    main()
