# Hugo - UserBot
#
# This file is a part of < https://github.com/TeamHugo/HugoAddons/>

"""
Fetch Random anime quotes

Command : `{i}aniquote`
"""

import requests

from . import *


@hugo_cmd(pattern="aniquote")
async def _(hg):
    u = await eor(hg, "...")
    try:
        resp = requests.get("https://animechan.vercel.app/api/random").json()
        results = f"**{resp['quote']}**\n"
        results += f" — __{resp['character']} ({resp['anime']})__"
        return await u.edit(results)
    except Exception:
        await u.edit("`Something went wrong LOL ...`")
