# Made by : @Arnab431 || github.com/ArnabXD
# Made For : https://github.com/TeamHugo/HugoAddons

"""
Search animes and manga from anilist.co using @animedb_bot

**༄** Commands Available
• `{i}manga <keyword>`
    To get manga info
"""

from telethon.errors import ChatSendInlineForbiddenError

from . import *

INLOCK = "`Seems like inline messages aren't allowed here`"


@hugo_cmd(
    pattern="manga ?(.*)",
)
async def manga(hg):
    msg = await eor(hg, "`Searching ...`")
    keyword = hg.pattern_match.group(1)
    if keyword is None:
        return await msg.edit("`Provide a Keyword to search`")
    try:
        animes = await hg.client.inline_query("animedb_bot", f"<m> {keyword}")
        await animes[0].click(
            hg.chat_id,
            reply_to=hg.reply_to_msg_id,
            silent=True if hg.is_reply else False,
            hide_via=True,
        )
        return await msg.delete()
    except Exception:
        return await msg.edit("`No Results Found ...`")
