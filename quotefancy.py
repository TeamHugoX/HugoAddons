# Hugo - UserBot
# Copyright (C) 2020 TeamHugo
#
# This file is a part of < https://github.com/TeamHugo/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHugo/Hugo/blob/main/LICENSE/>.


"""
**༄** Commands Available

• `{i}qfancy`
    Gets random quotes from QuoteFancy.com.
"""

from quotefancy import get_quote
from telethon.errors import ChatSendMediaForbiddenError

from . import *


@hugo_cmd(pattern="qfancy$")
async def quotefancy(e):
    mes = await eor(e, "`Processing...`")
    img = get_quote("img", download=True)
    try:
        await e.client.send_file(e.chat_id, img)
        os.remove(img)
        await mes.delete()
    except ChatSendMediaForbiddenError:
        quote = get_quote("text")
        await eor(e, f"`{quote}`")
    except Exception as e:
        await eor(e, f"**ERROR** - {str(e)}")
