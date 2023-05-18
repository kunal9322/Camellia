#CREATED BY @KIRITO1240
#API CREDITS: @KIRITO1240
#PROVIDED BY @NovaXMod

#IMPORTS
import requests as r
from pyrogram import *
from pyrogram.types import *

#BOT FILE IMPORTS
#Name -> Your Bots File Name (Eg. From Liaa import pbot as app)
from RUKA import pbot as app


#AI IMAGE GENERATION FUNCTION
@app.on_message(filters.command("aigen"), group=95)
async def generateai(_, message):
    if len(message.text.split()) < 2:
        return await message.reply_text("No Prompt Given!")
    textt = message.text.split(maxsplit=1)[1]
    b = await message.reply("Wait For 1-2 Mins Generating Your Image...")
    
    resp = r.post("https://ai-api-production.up.railway.app/ai", json={'promt': f'{textt}'}).json()
    
    a = resp['photo']
    await message.reply_photo(a, caption=f"**Generated BY:** @{app.me.username}\n🌀❤‍🩹")
    await b.delete()
    
__help__ = """
GENERATES AI IMAGES THROUGH API   
  
 â /aigen *:* GENERATES AI IMAGES THROUGH API """

__mod_name__ = "Aɪ IᴍɢGᴇɴ"
