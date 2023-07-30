import os
from pyrogram import Client, filters
import requests
from PIL import Image
app = Client("my_account")
idch = "*********"
idch2 = "************"
token1 = ''
token2 = '' 
@app.on_message(filters.chat('usd_iran'))
def log10(client, message):
    req = requests.session()
    mes = message.text
    try:
        qes = mes.split('@')[0]
        mesnah = qes + '@' +idch
        mesnah2 = qes + '@' +idch2
        req.get(f'https://api.telegram.org/{token1}/sendMessage?chat_id=-1001801425732&text='+mesnah)
        req.get(f'https://api.telegram.org/{token2}/sendMessage?chat_id=-1001984881370&text='+mesnah2)
    except:
        print("id dar message nist")
        mesnah = mes + '@' +idch


@app.on_message(filters.chat('lear_ir'))
def log(client, message):
    req = requests.session()
    mes2 = message.text
    try:
        qes2 = mes2.split('@')[0]
        mesnah21 = qes2 + '@' +idch
        mesnah22 = qes2 + '@' +idch2
        req.get(f'https://api.telegram.org/{token1}/sendMessage?chat_id=-1001801425732&text='+mesnah21)
        req.get(f'https://api.telegram.org/{token2}/sendMessage?chat_id=-1001984881370&text='+mesnah22)
    except:
        print("id dar message nist")
        mesnah = mes2 + '@' +idch


@app.on_message(filters.chat('cryptoprice_live'))
def log50(client, message):
    req = requests.session()
    mes25 = message.text
    try:
        qes25 = mes25.split('@')[0]
        mesnah51 = qes25 + '@' +idch
        mesnah52 = qes25 + '@' +idch2
        req.get(f'https://api.telegram.org/{token1}/sendMessage?chat_id=-1001801425732&text='+mesnah51)
        req.get(f'https://api.telegram.org/{token2}/sendMessage?chat_id=-1001984881370&text='+mesnah52)
    except:
        pass

@app.on_message(filters.chat('web3insider_fa'))
def log30(client, message):
    req = requests.session()
    api_url = f'https://api.telegram.org/{token1}/sendPhoto'
    mes3 = message.text
    file_id = message.photo.file_id
    downloaded_file = app.download_media(file_id)
    cap = message.caption
    cap = cap.split('.')[0]
    #---------------------------------------------#
    image = Image.open(downloaded_file)
    width, height = image.size
    bottom = height - (height - 573)
    cropped_image = image.crop((0, 0, width, bottom))
    cropped_image.save('cropped_image.jpg')
    #---------------------------------------------#
    with open('cropped_image.jpg', 'rb') as image_file:
        response = requests.post(api_url, data={'chat_id': "-1001801425732", 'caption': cap}, files={'photo': image_file})
        image_file.close()
    os.remove('cropped_image.jpg')


app.run()
