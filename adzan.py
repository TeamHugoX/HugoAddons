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
    LOKASI = "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"**Can't Find City** `{LOCATION}`", 120
        )
    result = json.loads(request.text)
    catresult = f"""
**Prayer Times Today:**
            
**📆 Date** `{result['items'][0]['date_for']}`
**📍 City** `{result['query']}` | `{result['country']}`

**Shurooq:** `{result['items'][0]['shurooq']}`
**Fajr:** `{result['items'][0]['fajr']}`
**Dhuhr:** `{result['items'][0]['dhuhr']}`
**Asr:** `{result['items'][0]['asr']}`
**Maghrib:** `{result['items'][0]['maghrib']}`
**Isha:** `{result['items'][0]['isha']}`
"""
    await eor(adzan, catresult)
