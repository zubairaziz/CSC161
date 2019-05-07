"""CSC 161 Project: Milestone IV

Milestone IV for the project.
Extra credit implemented:
- Object Oriented Design (tradinglib & filehandler)
- Modules (see tradinglib.py)
- Statistics (Has statistics that run at the end of every trading alg)

Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""

from filehandler import Filehandler
from tradinglib import TradingLibrary


def main():
    results = {'alg_moving_average': [], 'alg_mine': []}

    stock_trader = TradingLibrary()
    print('Testing for alg_moving_average()')
    stock_trader.alg_moving_average()
    print(stock_trader)
    results['alg_moving_average'] = [
        stock_trader.cash_balance, stock_trader.total_bought]

    print('Testing for alg_mine()')
    stock_trader.alg_mine()
    print(stock_trader)
    results['alg_mine'] = [
        stock_trader.cash_balance, stock_trader.total_bought]

    print_stats(stock_trader, results)


def print_stats(trader, results):
    print('\n\t----- ----- ----- -----')
    print('Statistics for this run...')
    print('{0}'.format(trader.file))
    print('Historic low for this stock: ${0:.2f}'.format(
        trader.historic_low))
    print('Historic high for this stock: ${0:.2f}'.format(
        trader.historic_high))
    print('\nFor moving average algorithm...')
    print('Cash balance: ${0:.2f}'.format(
        results['alg_moving_average'][0]))
    print('Stocks bought: {0} shares'.format(
        results['alg_moving_average'][1]))
    print('\nFor my custom algorithm...')
    print('Cash balance: ${0:.2f}'.format(
        results['alg_mine'][0]))
    print('Stocks bought: {0} shares'.format(
        results['alg_mine'][1]))
    print(
        '\nMy own algorithm bought {0} more stocks than the moving average and made ${1:.2f} more money'.format(
            (results['alg_mine'][1]) -
            (results['alg_moving_average'][1]),
            (results['alg_mine'][0]) -
            (results['alg_moving_average'][0])
        ))
    print('\t----- ----- ----- -----\n')


if __name__ == '__main__':
    main()
