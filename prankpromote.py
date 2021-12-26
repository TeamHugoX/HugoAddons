# Written By @senku_ishigamiii and inspiried from DarkCobra Wala Plugin

"""
**༄** Commands Available

• `{i}pprank`
    Show Fake Promotion
"""

import asyncio

from . import *


@hugo_cmd(pattern="pprank")
async def pprank(hg):
    msg = await eor(hg, "**PROMOTING USER..**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTING USER...**")
    await asyncio.sleep(1)
    await msg.edit("**GIVING RIGHTS**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTED USER SUCCESSFULLY**")
