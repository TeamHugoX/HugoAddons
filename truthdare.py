# Hugo - UserBot
# Copyright (C) 2020 TeamHugo
#
# This file is a part of < https://github.com/TeamHugo/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHugo/Hugo/blob/main/LICENSE/>.

"""
**༄** Commands Available -

• `{i}truth`
   `Get Truth Task.`

• `{i}dare`
   `Get Dare Task.`
"""

import requests as r
from bs4 import BeautifulSoup as bs

from . import *

link = "https://fungenerators.com/random/truth-or-dare?option="


@hugo_cmd(pattern="truth$")
async def gtruth(hg):
    m = await eor(hg, "`Generating a Truth Statement.. `")
    nl = link + "truth"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#TruthTask**\n\n`{cm}`")


@hugo_cmd(pattern="dare$")
async def gtruth(hg):
    m = await eor(hg, "`Generating a Dare Task.. `")
    nl = link + "dare"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#DareTask**\n\n`{cm}`")
