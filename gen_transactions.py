"""get_transactions

Generates transactions for our hcoin. They will
be consumed by hcoin.py cmd client.
We need to provide a users's list and depending on other
variables as the start/end date, number of transactions per day and
number of transactions in total the result will always be different.
As part of our spec, zero or more transactions need take place every day,
and each user migh be in more than one transactions per day. Users cannot
initiate transactions to themselves

"""

import random

USERS_LIST = ['markos', 'nikos', 'panagiota', 'kostas', 'dana', 'nikos',
              'maria', 'chris', 'david', 'insurance', 'supermarket', 'grocery']
START_DATE = "2011-06-06"
END_DATE = "2017-10-18"
# transactions allowed per day are zero up to this number
MAX_TRANSACTIONS_PER_DAY = 10
# max number of transactions to generate. If start/end date are very close,
# and there's a low MAX_TRANSACTIONS_PER_DAY number, this won't be reached
NUMBER_OF_TRANSACTIONS = 10000000
# transactions need be integers and up to this amount
MAX_TRANSACTION_PRICE = 100
TRANSACTIONS_FILE = 'transactions.txt'


def generate_transactions():
    """
    Generate transactions

    """
    start_year, start_month, start_day = map(int, START_DATE.split("-"))
    end_year, end_month, end_day = map(int, END_DATE.split("-"))
    # a simple counter
    generated_transactions = 0
    # the list with transactions
    transactions = []
    for year in range(start_year, end_year+1):
        for month in range(1, 12 + 1):
            for day in range(1, 31 + 1):
                # we want to generate valid transactions, so we take
                # under consideration that Feb has 28 days, while
                # some of the other months have 30 and others 31
                if not ((day == 31 and month in [2, 4, 6, 9, 11])
                        or (month == 2 and day in [29, 30, 31])):
                    # we generate 0 to the number defined as of max
                    # transactions per day, and this is a random number.
                    # Part of our spec is that
                    # some days don't have transactions
                    for i in range(0, random.randint(
                                   0, MAX_TRANSACTIONS_PER_DAY)):
                        random_sender = USERS_LIST[random.randint(
                                                   0, len(USERS_LIST)-1)]
                        random_receiver = USERS_LIST[random.randint(
                                                     0, len(USERS_LIST) - 1)]
                        # make sure this is not the same, as a user cannot
                        # send an amount to themselves.
                        # This is part of our spec

                        # TODO: optimize the check
                        if random_sender != random_receiver:
                            transaction = "%s-%s-%s,%s,%s,%s" % (
                                year,
                                # day and month contain two digits, eg 01
                                str(month).zfill(2),
                                str(day).zfill(2),
                                random_sender,
                                random_receiver,
                                random.randint(1, MAX_TRANSACTION_PRICE))
                            # increase counter
                            generated_transactions += 1
                            transactions.append(transaction)
                            # perform length check
                            if len(transactions) > NUMBER_OF_TRANSACTIONS:
                                return transactions
    print('total transactions generated: %s' % generated_transactions)
    return transactions


if __name__ == "__main__":
    """
    Generate transactions, taking under consideration the different variables
    at the beginning of this file

    Once transactions are generated they are stored on a file specified
    """
    transactions = generate_transactions()
    transactions_string = '\n'.join(transactions)
    try:
        # error handling. Things can go wrong here, as
        # trying to write to a file with no permissions
        # eg as a user on /
        file = open(TRANSACTIONS_FILE, 'w')
        file.write(transactions_string)
        file.close()
    except IOError as exc:
        print("Error: Problem saving to file", exc)
