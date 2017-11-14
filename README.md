# hcoin
hcoin - a non scalable fictional currency . ICO soon to come ;)

## What is it

Introducing hcoin - a non scalable fictional currency!

All system users start with a balance of 0. Then for each transaction they either give out
hcoins to other users (in this case they have their balance decreased), or they accept hcoins
(in this case they have their balance increased)

## Ledger format

Transactions have the following format:

    2017-11-11,maria,nikos,54
    2017-12-24,nikos,insurance,88

which translates to:

    date,transaction_sender,transaction_receiver,amount


## Requirements for the hcoin client:

user current balance need be available but also balance for a specific time in the past.
users are identified through a username
initial balance for all users is zero
amounts are integers, and a limit is specified - currently this is 100
transactions might occur every day but this is not necessary. there might be days with no transactions
a user can send/receive amounts within the same day

## How to install

No need to install anything, only need python2 or python3.

Clone the repository:

    user@user:/tmp$ git clone https://github.com/mgogoulos/hcoin
    user@user:/tmp$ cd hcoin

and run hcoin.py, this will get you some examples:

    user@user:/tmp/hcoin$ python hcoin.py
    hcoin show balance

    Usage: hcoin.py all - will output balance for all users
    Usage: hcoin.py user - will output balance for user
    Usage: hcoin.py user date - will output balance for user, for that date

    Example: hcoin.py user 2017-01-04 - will output balance for user,  for that date

## Tests
To run the tests install pytest lib, either globally or inside a virtualenv.

Currently pytest is the only dependency on requirements.txt:

    user@user:/tmp/hcoin$ virtualenv .
    user@user:/tmp/hcoin$ ./bin/pip install -r requirements.txt
    user@user:/tmp/hcoin$ ./bin/pytest tests.py


