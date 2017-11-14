# hcoin
Introducing hcoin - a non scalable fictional currency . ICO soon to come ;)

## Brief introduction

All system users start with a balance of 0. Then for each transaction they either give out
hcoins to other users (in this case they have their balance decreased), or they accept hcoins
(in this case they have their balance increased)


Transactions have the following format:

    2017-11-11,maria,nikos,54
    2017-12-24,nikos,insurance,88

which translate to:

    date,transaction_sender,transaction_receiver,amount


## Requirements for the hcoin client

* user current balance need be available but also balance for a specific time in the past.
* users are identified through a username
* initial balance for all users is zero
* amounts are integers, and a limit is specified - currently this is 100
* transactions might occur every day but this is not necessary. there might be days with no transactions
* a user can send/receive amounts within the same day

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

## Examples

If you run hcoin with the transactions.txt included you will get the following output

Get balance for all users:

    user@user:/tmp/hcoin$ python hcoin.py all
    User / Balance

    markos -3895
    nikos -2612
    insurance -2097
    grocery -1504
    dana -1413
    supermarket -1295
    panagiota -569
    chris 669
    kostas 2162
    david 3431
    maria 7123

Get balance for user chris:

    user@user:/tmp/hcoin$ python3 hcoin.py chris
    User / Balance

    chris 669

Get balance for user chris for date 2015-11-11:

    user@user:/tmp/hcoin$ python hcoin.py chris 2015-11-11
    User / Balance for the date of 2015-11-11

    chris -1199


## How to produce the transactions

Use gen_transactions.py file, after editing default variables. There's plenty
of documentation to direct you:

    user@user:/tmp/hcoin$ python gen_transactions.py
    total transactions generated: 11525

    user@user:/tmp/MARKOS/hcoin$ head transactions.txt
    2011-01-01,chris,dana,89
    2011-01-01,nikos,dana,68
    2011-01-01,panagiota,kostas,35
    2011-01-01,kostas,nikos,71
    2011-01-01,david,chris,90
    2011-01-01,david,maria,40
    2011-01-01,nikos,insurance,17
    2011-01-01,david,grocery,59
    2011-01-02,supermarket,dana,17
    2011-01-02,david,supermarket,100
...

## Tests
To run the tests install pytest lib, either globally or inside a virtualenv.

Currently pytest is the only dependency on requirements.txt:

    user@user:/tmp/hcoin$ virtualenv .
    user@user:/tmp/hcoin$ ./bin/pip install -r requirements.txt
    user@user:/tmp/hcoin$ ./bin/pytest tests.py


### hcoin's custom image
<p align="center">
  <img src="https://raw.githubusercontent.com/mgogoulos/hcoin/master/hcoin.jpg?raw=true" alt="Hcoin logo made with logojoy.com"/>
</p>