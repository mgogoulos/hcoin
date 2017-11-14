"""hcoin

Processes a ledger in a specific format and returns balance.
Example format is "2011-01-05,chris,nikos,28"
Using the cmd it can return balance for all users, or for
a specific user. Specific user balance for a date is also possible

"""

import sys
from datetime import date

# file with generated transactions
from gen_transactions import TRANSACTIONS_FILE

# this will be the global list of users
users = []


class User(object):
    """
    The user object

    User instances are initiated with the username
    Initial balance for all users is zero.
    For each transaction we store the current balance
    This is not persistent!

    >>> from hcoin import populate_user_records, User, read_transactions, users
    >>> transactions = read_transactions()
    >>> populate_user_records(transactions)

    >>> users
    [<User: username=panagiota, total_balance=392 ...>,
    <User: username=nikos, total_balance=-4953 ...>,
    <User: username=grocery, total_balance=1681 ...>]

    """
    def __init__(self, username):
        """
        Initiate with username
        """
        self.username = username
        self.total_balance = 0
        self.record = {}

    def set_balance(self, date, amount):
        """
        Sets a new balance

        Accepts the date and amount for a transaction where
        user is affected. Then save new balance and keep a
        record on what what the balance for that date.

        >>> u
        <User: username=kostas, total_balance=-376 ...>
        >>> u.total_balance
        -376

        >>> u.set_balance('2017-11-15', 600)
        >>> u.total_balance
        224

        >>> u.record['2017-11-15']
        224

        >>> u.record['2017-11-14']
        >>> -376

        """

        self.total_balance = self.total_balance + amount
        self.record[date] = self.total_balance

    def get_balance_for_date(self, transaction_date):
        """
        Return balance for a specific date
        If there is a record for the exact date, then return the balance
        at that time

        >>> u
        <User: username=kostas, total_balance=86 ...>

        >>> u.get_balance_for_date('2011-03-03')
        -624

        On the current transactions.txt there's an entry for this date
        (2011-03-03,david,kostas,77)

        But no entry for this date

        >>> u.get_balance_for_date('2011-03-04')
        -624

        So it brings last entry, which is '2011-03-03'

        Now we try for date '2011-03-06'

        >>> u.get_balance_for_date('2011-03-06')
        -624

        Where there's an entry there indeed
        (2011-03-06,nikos,kostas,1)
        """

        if self.record.get(transaction_date):
            return self.record.get(transaction_date)
        else:
            # if there is no record for the date, we'll still return the
            # balance for that time. That would be the balance at the closest
            # date before that, that we have a record
            r_dates = sorted([d for d in self.record.items()
                              if d[0] < transaction_date])
            # this will be a sorted list with record dates and balance
            # at that time
            # example [('2017-05-28', 4289), ('2017-05-29', 4227)]
            if r_dates:
                # return the balance for the last date we have a record
                return r_dates[-1][1]
            else:
                return 0

    def __repr__(self):
        return (('<User: username=%s, total_balance=%s ...>')
                % (self.username, self.total_balance))


def get_or_create_user(username=''):
    """
    Return a user

    User list is generated on populate_user_records.
    A list of users available as users is generated
    Given a username, check if this exists on users,
    otherwise create an instance and append to users

    >>> from hcoin import User, users, get_or_create_user
    >>> from hcoin import populate_user_records, read_transactions
    >>> transactions = read_transactions()
    >>> populate_user_records(transactions)
    >>> users
    [<User: username=panagiota, total_balance=2011 ...>,
     <User: username=dana, total_balance=5787 ...>,
    ...

    This user exists
    >>> u = get_or_create_user('markos')
    >>> u
    <User: username=markos, total_balance=-721 ...>

    While this will be created
    >>> u = get_or_create_user('not_existing')
    >>> u
    <User: username=not_existing, total_balance=0 ...>


    """
    user = None
    for u in users:
        if u.username == username:
            user = u
            break
    if not user:
        user = User(username)
        users.append(user)
    return user


def populate_user_records(transactions):
    """
    Get list of transactions and populate users list and update user balances
    For a given transaction increase the balance for the receiver,
    while decrease the balance for the sender
    """

    for transaction in transactions:
        try:
            transaction_date, transaction_sender, transaction_receiver, \
                amount = transaction.split(',')

            sender = get_or_create_user(transaction_sender)
            receiver = get_or_create_user(transaction_receiver)

            sender.set_balance(transaction_date, -int(amount))
            receiver.set_balance(transaction_date, int(amount))
        except ValueError:
            # do not break if a line on the transactions file is incorrect
            pass


def read_transactions():
    """
    Read a file containing transactions,
    return list of transactions
    """
    with open(TRANSACTIONS_FILE) as f:
        transactions = f.readlines()
    return transactions


def help(argv):
    print("hcoin show balance\n\n")
    print("Usage: %s all - will output balance for all users" % argv[0])
    print("Usage: %s user - will output balance for user" % argv[0])
    print("Usage: %s user date - will output balance for user, "
          "for that date\n" % argv[0])
    print("Example: %s user 2017-01-04 - will output balance for user, "
          " for that date" % argv[0])

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        # show help and exit
        help(sys.argv)
        sys.exit(0)
    # read list of transactions
    transactions = read_transactions()

    # populate users list with records
    populate_user_records(transactions)

    if len(sys.argv) == 2:
        # show balance for specified or all users
        username = sys.argv[1]
        if username == 'all':
            # show balance for all users
            print('User / Balance\n')
            # sort per total_balance
            users = sorted(users, key=lambda u: u.total_balance)

            for user in users:
                print("%s %s" % (user.username, user.total_balance))
        else:
            # show balance for specified users
            print('User / Balance\n')
            user = get_or_create_user(username)
            print("%s %s" % (user.username, user.total_balance))

            # show output for user
    elif len(sys.argv) == 3:
        # show balance for specified user for a specific date
        username = sys.argv[1]
        if username == 'all':
            print('Cannot show balance for all users for a specified date.'
                  'This is scheduled for a future release')
            sys.exit(0)

        transaction_date = sys.argv[2]
        try:
            # perform a check that this is valid date format
            # and also set the month/day to 2 char lenght, as this
            # is the format stored on transactions
            y, m, d = transaction_date.split('-')
            y = int(y)
            m = int(m.zfill(2))
            d = int(d.zfill(2))
            transaction_date = date(y, m, d).isoformat()
        except:
            print('wrong format, need something like 2017-05-11.'
                  ' Ignoring date')
            print('User / Balance\n')
            user = get_or_create_user(username)
            print("%s %s" % (user.username, user.total_balance))

            sys.exit(0)
        # we are good to go, show output for user for specific date
        print('User / Balance for the date of %s\n' % transaction_date)
        user = get_or_create_user(username)
        print("%s %s" % (user.username,
              user.get_balance_for_date(transaction_date)))
