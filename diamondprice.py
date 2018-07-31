from caratsize import caratsize
from colornumber import colornumber
from rportconnect import connectdb, cutstring




#c = conn.cursor() # mark the cursor in database
#c.execute("select * from rapaport") # get all data from table->rapaport
#rows = c.fetchall() # assign data in rows

#seealldata(rows)
#x = '1'
#while x == '1':
#    diamondshape = input("Round (r) or Pear (p): ")
#    carat = input("please enter the carat size: ")
def diamondprice(diamondshape,carat,color,clarity,discount,caratport=0):
    conn = connectdb('_rRapaport')
    carat = float(carat)
    if caratport != '':        
        caratport = caratsize(caratport)
        caratportf = float(caratport)
    else:
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
    currency = 33.3
    calprice = 0.0
    calprice = newprice * carat * currency * newdiscount
#    print("rapaport = {}".format(newprice))
#    print("calcurate price = {}".format(round(calprice, 3)))
#    print("carat weight = {}".format(carat))
#    print("currency rate = {}".format(currency))
#    print("discount rate = {}%".format(discount))
#    print("---------"*10)
#    seealldata(rows)
    #x = input("do you want more (1) or no more (0): ")
    conn.close()
    return calprice,caratport,newprice,currency
    