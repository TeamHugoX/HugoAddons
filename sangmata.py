# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

"""
**༄** Commands Available -
• `{i}sg (reply to user/message)`
   View people's name history.
"""

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from . import *


@hugo_cmd(pattern="sg(u)?(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(event, "**Please Reply To User Messages.**", 90)
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    hugo = await eor(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/search_id {uid}")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(hugo, "**This Person Has Never Changed His Name**", 90)
    if "No records found" in responses:
        await edit_delete(hugo, "**This Person Has Never Changed His Name**", 90)
    names, usernames = await sangamata_seperator(responses)
    cmd = event.pattern_match.group(1)
    x = None
    check = usernames if cmd == "u" else names
    for i in check:
        if x:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            x = True
            await hugo.edit(i, parse_mode=_format.parse_pre)


async def sangamata_seperator(sanga_list):
    for i in sanga_list:
        if i.startswith("🔗"):
            sanga_list.remove(i)
    s = 0
    for i in sanga_list:
        if i.startswith("Username History"):
            break
        s += 1
    usernames = sanga_list[s:]
    names = sanga_list[:s]
    return names, usernames
