from flask import Flask, request
import json
import requests
from diamondprice import diamondprice
from placevalue import placevalue
from rportconnect import connectdb
#from writeindb import writeindb

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer D7ZfjxRtPswUt5MWU96sqt69tRDlUTDp4YlRmn34Td3pa1g+mZTHItrAUAgMJiOmM6y65eOZVJmK+3XqiZ7bGe4JJy/pUTfqTXdERJWqiuUNI487QyFK2sNknl7b9T2wqfl2ZKe585iCQNx8Kos0kQdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server for test bot.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    #msg_in_string = json.dumps(msg_in_json)
#    writeindb(msg_in_json)    
#    with open('datacollection.json', 'w') as writefile:
#        json.dump(msg_in_json, writefile)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID = msg_in_json["events"][0]['source']['userId']
    msgType = msg_in_json["events"][0]['message']['type']
    if msgType == 'group':
        groupID = msg_in_json["events"][0]['source']['groupId']
    else:
        groupID = '00000000'
        
    textMsg = msg_in_json["events"][0]['message']['text']
    textType =msg_in_json["events"][0]['message']['type']
    textId = msg_in_json["events"][0]['message']['id']
    conn = connectdb('_rRapaport')
    tablename = 'collectiondata'
    c = conn.cursor()
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS '{}'(userID TEXT, msgType TEXT, groupID TEXT, textMsg TEXT, textType TEXT, textId TEXT)".format(tablename))
    
    def data_entry():
        c.execute("INSERT INTO '{}' VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(tablename, userID, msgType, groupID, textMsg, textType, textId))
        conn.commit()
        c.close()
        conn.close()
    
#    create_table()
    data_entry()    
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
#    if msgType != 'text':
#        reply(replyToken, ['Only text is allowed.'])
#        return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    textstart = text[0]
    
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # if text in response_dict:
    #     replyQueue.append(reponse_dict[text])
    # else:
    #     replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')
       
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])
   
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    #replyQueue.append('นี่คือรูปแบบข้อความที่รับส่ง')
    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    if textstart == '/':  
        #text = '/r,2.34,d,vvs1,30'
        diamondshape = text.split(',')[0]
        diamondshape = diamondshape[1]
        carat = text.split(',')[1]
        color = text.split(',')[2]
        clarity = text.split(',')[3]
        discount = text.split(',')[4]
        price = diamondprice(diamondshape,carat,color,clarity,discount)
        newprice = placevalue(price['calprice'])
        newpriceusd = placevalue(price['calpriceusd'])
#        calprice,caratport,newprice,rate
#        replyQueue.append(diamondshape)
#        replyQueue.append(carat)
#        replyQueue.append(color)
#        replyQueue.append(clarity)
        newpriceusdtext = 'total price is {} USD'.format(newpriceusd)
        newpricetext = 'total price is {} THB'.format(newprice)
        rapaportpricetext = 'the rapaport is {}'.format(price['rapaportprice'])
        currencytext = 'the superrich rate is {}'.format(price['currency'])
        discounttext = 'the discount is {}%'.format(price['discount'])
        replyQueue.append(newpriceusdtext)
        replyQueue.append(newpricetext)
        replyQueue.append(rapaportpricetext)
        replyQueue.append(currencytext)
        replyQueue.append(discounttext)
        reply(replyToken, replyQueue[:5])        
        return 'OK', 200
    elif textstart == '=':
        #text = '=111111111,222222222'
        price1 = text.split(',')[0]
        price1 = price1[1:]
        price2 = text.split(',')[1]
        price1 = float(price1)
        price2 = float(price2)
        totalprice = price1+price2
#        print(totalprice)
        totalpricetext = 'total price is {}'.format(totalprice)
        replyQueue.append(totalpricetext)
        reply(replyToken, replyQueue[:5])
        return 'OK', 200
    else:
#        replyQueue.append('please start with / for asking bot')
#        reply(replyToken, replyQueue[:5]) 
        return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
