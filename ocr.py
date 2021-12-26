#
# Hugo - UserBot
#
# This file is a part of < https://github.com/TeamHugo/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHugo/Hugo/blob/main/LICENSE/>.
#


"""
**༄** Commands Available -

• `{i}ocr <language code><reply to a photo>`
    text recognition service.

"""


import requests as r
from telegraph import upload_file as uf

from . import *

TE = f"API not found, Please get it from ocr.space and set\n\ncommand `{HNDLR}setredis OCR_API your-api-key`"


@hugo_cmd(pattern="ocr ?(.*)")
async def ocrify(hg):
    if not hg.is_reply:
        return await eor(hg, "`Reply to Photo...`")
    msg = await eor(hg, "`Processing..`")
    OAPI = udB.get("OCR_API")
    if not OAPI:
        return await msg.edit(TE)
    pat = hg.pattern_match.group(1)
    repm = await hg.get_reply_message()
    if not (repm.media and repm.media.photo):
        return await msg.edit("`Not a Photo..`")
    dl = await repm.download_media()
    if pat:
        atr = f"&language={pat}&"
    else:
        atr = "&"
    tt = uf(dl)
    li = "https://telegra.ph" + tt[0]
    gr = r.get(
        f"https://api.ocr.space/parse/imageurl?apikey={OAPI}{atr}url={li}"
    ).json()
    trt = gr["ParsedResults"][0]["ParsedText"]
    await msg.edit(f"**🎉 OCR PORTAL\n\nRESULTS ~ ** `{trt}`")
