"""

Using MAth.floor method in get_number_of_bills(budget, denomination)
"""
import math

def exchange_money(budget, exchange_rate):
    """

    :param: budget: float - amount of money you are planning to exchange.
    :param: exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return float(budget/exchange_rate)


def get_change(budget, exchanging_value):
    """

    :param: budget: float - amount of money you own.
    :param: exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return float(budget-exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """

    :param: denomination: int - the value of a bill.
    :param: number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return int(denomination*number_of_bills)


def get_number_of_bills(budget, denomination):
    """

    :param: budget: float - the amount of money you are planning to exchange.
    :param: denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return math.floor(budget/denomination)


def get_leftover_of_bills(budget, denomination):
    """

    :param: budget: float - the amount of money you are planning to exchange.
    :param: denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return float(budget % denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param: budget: float - the amount of your money you are planning to exchange.
    :param: exchange_rate: float - the unit value of the foreign currency.
    :param: spread: int - percentage that is taken as an exchange fee.
    :param: denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exchange_rate_with_spread = exchange_rate + spread*exchange_rate/100
    new_budget = exchange_money(budget, exchange_rate_with_spread)
    number_of_bills_on_new_budget = get_number_of_bills(new_budget, denomination)
    final_exachangabe_value = get_value_of_bills(number_of_bills_on_new_budget, denomination)

    return final_exachangabe_value
