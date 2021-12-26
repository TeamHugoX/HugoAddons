# Hugo - Userbot
# 2021 copyright (C)

"""
**༄** Commands Available -
• `{i}adzan (city)`
   Seeing the time for the call to prayer, prayer.
"""

import requests
from . import *


@hugo_cmd(pattern="adzan ?(.*)")
async def get_adzan(adzan):
    "Shows you the Islamic prayer times of the given city name"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus("WEATHER_DEFCITY") or "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"**Can't Find City** `{LOCATION}`", 120
        )
    result = json.loads(request.text)
    catresult = f"<b>Jadwal Shalat Hari Ini:</b>\
            \n<b>📆 Date </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 City</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>Shurooq  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>Fajr : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>Dhuhr  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>Asr  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>Isha : </b><code>{result['items'][0]['isha']}</code>\
    "
    await eor(adzan, catresult)
