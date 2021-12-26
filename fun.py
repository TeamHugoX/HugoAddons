# Hugo - UserBot
# Copyright (C) 2020 TeamHugo
#
# This file is a part of < https://github.com/TeamHugo/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHugo/Hugo/blob/main/LICENSE/>.

"""
**༄** Commands Available

• `{i}joke`
    To get joke.

• `{i}insult`
    Insult someone..

• `{i}url <long url>`
    To get a shorten link of long link.

• `{i}decide`
    Decide something.

• `{i}xo`
    Opens tic tac game only where using inline mode is allowed.

• `{i}wordi`
    Opens word game only where using inline mode is allowed.

• `{i}gps <name of place>`
    Shows the desired place in the map.

"""

import random

import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError

from . import *


@hugo_cmd(pattern="joke$")
async def _(hg):
    await eor(hg, get_joke())


@hugo_cmd(pattern="insult$")
async def gtruth(hg):
    m = await eor(hg, "Generating...")
    nl = "https://fungenerators.com/random/insult/new-age-insult/"
    ct = requests.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"{cm}")


@hugo_cmd(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await eor(event, "Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(
            event,
            "**Shortened url**==> {}\n**Given url**==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await eor(event, "`Something went wrong. Please try again Later.`")


@hugo_cmd(pattern="decide$")
async def _(event):
    hm = await eor(event, "`Deciding`")
    r = requests.get("https://yesno.wtf/api").json()
    try:
        await event.reply(r["answer"], file=r["image"])
        await hm.delete()
    except ChatSendMediaForbiddenError:
        await eor(event, r["answer"])


@hugo_cmd(pattern="xo$")
async def xo(hg):
    xox = await hg.client.inline_query("xobot", "play")
    await xox[random.randrange(0, len(xox) - 1)].click(
        hg.chat_id, reply_to=hg.reply_to_msg_id, silent=True, hide_via=True
    )
    await hg.delete()


@hugo_cmd(pattern="wordi$")
async def word(hg):
    game = await hg.client.inline_query("wordibot", "play")
    await game[0].click(
        hg.chat_id, reply_to=hg.reply_to_msg_id, silent=True, hide_via=True
    )
    await hg.delete()


@hugo_cmd(pattern="gps (.*)")
async def map(hg):
    get = hg.pattern_match.group(1)
    if not get:
        return await eor(hg, "Use this command as `.gps <query>`")
    gps = await hg.client.inline_query("openmap_bot", f"{get}")
    await gps[0].click(
        hg.chat_id, reply_to=hg.reply_to_msg_id, silent=True, hide_via=True
    )
    await hg.delete()
