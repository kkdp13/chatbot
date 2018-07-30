from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('lkzh0jXv/E/35u+xA02IyrMt7+M0xUMBTvuwa9rHWMP8LAgeGuRXYdyuSWHO/yDJPjRm0yB409b142EY0nEukr1+Rdy2HoXRX2TWYn7jYL52X9GKL3/wHrKdtGjndL9u7UsUDkid8/T7IsjD6VV7LgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1cbf55924eabba81f5046f7021e4dc1f')

@app.route('/')
def index():
    return 'This is chatbot server.'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
 
