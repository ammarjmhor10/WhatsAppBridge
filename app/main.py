import os
from telebot import TeleBot,custom_filters,types
from flask import Flask, request
import json
import requests
from database.ViewModel import FileID
from WhatsApp.whatsApp import reply_message
from Tele import tele
from database import Model
import os 
from dotenv import load_dotenv
load_dotenv()
bot = tele.bot

secret = os.environ.get("SECRET")

app = Flask(__name__)

SUDO_ID = "259127202"
chat ='-789422554'



def varify_token(par:dict):
    if secret == par['hub.verify_token']:
        return par['hub.challenge']
            



@app.route('/whatsapp',methods=['GET','POST'])
def whatsapp():
    par = request.args
    if par:
        par = varify_token(par)
        return par
    else: 
        data = json.loads(request.get_data().decode('utf-8'))

        try:
            FileID(data)
            return '200'
        except Exception as e:
            print(data)
            print(e)
            return '400'


@app.route("/", methods=['GET'])
def index():
    return "from WhatsApp " 

# API in Telegram by Get this URL
@app.route("/webhook",methods=["GET"])
def webhook():
    url_https = str(request.url_root).replace('http','https')
    bot.remove_webhook()
    bot.set_webhook(url=url_https)
    return url_https


#proccess new response from Telegram POST Json 
@app.route('/', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    bot.add_custom_filter(custom_filters.IsReplyFilter())
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200




if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.IsReplyFilter())
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
