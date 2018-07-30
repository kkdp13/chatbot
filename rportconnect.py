import sqlite3
from caratsize import caratsize
from colornumber import colornumber

# connect database by db_file
# have to put database in save folder of python file



def connectdb(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# see all data in database table
def seealldata(rows):
    for row in rows:
        print(row)

# cut unwanted string
def cutstring(price):
    price = str(price)
    price = price.strip("(")
    price = price.strip(",)")
    # print(price)
    return price
