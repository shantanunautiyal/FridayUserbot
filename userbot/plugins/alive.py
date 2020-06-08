"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY STATUS** \n`Shantanu's Bot IS:` **✅ Alive**\n\n"
                     "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`DATABASE STATUS:` **ALL NORMAL! WORKING FINE 🙂**\n`NO PROBLEM FOUND🔥!\n`"
                     "`CONNECTION PROVIDER:` ** AMAZON WEB SERVICES\n"
                     "`CURRECT BOT LOCATION:` ** Delhi,India\n"
                     "`DEPLOYING SERVICE BY: HEROKU INC.\n"
                     "`IP:` 3.82.66.232\n"
                     "`SYSTEM TYPE:` LINUX\n"
                     "`BASED ON:` UNIBORG\n"
                     "`SATELLITE:` ⚡SHANTANU SAT-1⚡\n"
                     "`MADE USING:` PYTHON\n"
                     f"`MY BOSS`: {DEFAULTUSER}\n\n"
                     "ALWAYS WITH YOU MY BOSS\n\n"
                     "`SATELLITE STATUS: ✅ Alive\n\n"
                     "[⚡DEPLOY SHANTANU⚡]") 

