# Hugo - Userbot
# 2021 copyright (C)
# Ported by OMGHelo <https://github.com/OMGHelo>

"""
**༄** Commands Available -
• `{i}p`
   Saying Islamic greetings.

• `{i}y`
   Responding to Islamic greetings.

• `{i}k`
   Say hello to Christianity.
"""

from . import *


@hugo_cmd(pattern="p ?(.*)")
async def _(event):
    await eor(event, "**Assalamualaikum warahmatullahi wabarakatuh**")


@hugo_cmd(pattern="y ?(.*)")
async def _(event):
    await eor(event, "**Waalaikumsalam warahmatullahi wabarakatuh**")


@hugo_cmd(pattern="k ?(.*)")
async def _(event):
    await eor(event, "**Shalom Aleichem**")
    
