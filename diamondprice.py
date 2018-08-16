from caratsize import caratsize
from colornumber import colornumber
from rportconnect import connectdb, cutstring
from placevalue import placevalue
from getcurrency import getcurrency

#c = conn.cursor() # mark the cursor in database
#c.execute("select * from rapaport") # get all data from table->rapaport
#rows = c.fetchall() # assign data in rows

#seealldata(rows)
#x = '1'
#while x == '1':
#    diamondshape = input("Round (r) or Pear (p): ")
#    carat = input("please enter the carat size: ")
def diamondprice(diamondshape,carat,color,clarity,discount):
    conn = connectdb('_rRapaport')
    carat = float(carat)
    caratport = caratsize(carat)
    caratportf = float(caratport)
    #print(caratportf)
    #color = input("please enter the color of diamond: ")
    colorcode = colornumber(color)
    #clarity = input("please enter the clarity of diamond: ")
    #discount = input("please enter the discount without % (2 digit): ")
    newdiscount = float(discount)
    if clarity == 'if':
        clarity = 'vif'
    if diamondshape == 'r':
        c = conn.cursor()
        c.execute("select {} from rapaport where carat = {}".format(clarity, caratportf))
    else:
        c = conn.cursor()
        c.execute("select {} from prapaport where carat = {}".format(clarity, caratportf))
    rows = c.fetchall()
    price = rows[colorcode]
    #print(rows[colorcode])
    #print(rows)
    newprice = cutstring(price)
    newprice = float(newprice)
    carat = float(carat)
    newdiscount = 1 + (newdiscount / 100)
    currency = 0.0
    currency = float(getcurrency())
    calprice = 0.0
    calpriceusd = 0.0
    calpriceusd = newprice * carat * newdiscount
    calprice = calpriceusd * currency
    rapaportprice = placevalue(newprice)
#    print("rapaport = {}".format(rapaportprice))
#    print("calcurate price = {}".format(round(calprice, 3)))
#    print("carat weight = {}".format(carat))
#    print("currency rate = {}".format(currency))
#    print("discount rate = {}%".format(discount))
#    print("---------"*10)
#    seealldata(rows)
    #x = input("do you want more (1) or no more (0): ")
    print(currency)
    conn.close()
    returndic = dict()
    returndic['calprice'] = calprice
    returndic['rapaportprice'] = rapaportprice
    returndic['currency'] = currency
    returndic['discount'] = discount
    returndic['calpriceusd'] = calpriceusd
    return returndic
    
#diamonprice = diamondprice('r',1.05,'h','vs1',-25)
#print(diamondprice)