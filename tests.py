import unittest
from datetime import date

from hcoin import populate_user_records, read_transactions
from hcoin import User, users, get_or_create_user


class UserTest(unittest.TestCase):

    def testNewUser(self):
        user = get_or_create_user('not_existing_user')
        self.assertEqual(user.total_balance, 0)

    def testSetUserBalance(self):
        user = get_or_create_user('not_existing_user')
        user.set_balance(date.today(), 200)
        self.assertEqual(user.total_balance, 200)


if __name__ == '__main__':
    unittest.main()
