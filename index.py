import os
import json
import discord
from discord.ext import commands

# GLOBAL CONSTANTS
f = open("config.json")
CONFIG = json.load(f)
f.close()

EMBEDCOLOR = 0xFCD03F
DEVGUILDS = CONFIG["devguilds"]
CRYPTOCOMPARECOINCHOICES = ["BTC", "BCH", "ETH", "LTC", "DOGE", "XMR", "BNB"]
CRYPTOCOMPARECURRENCYCHOICES = [
    "USD",
    "EUR",
    "AUD",
    "GBP",
    "JPY",
    "CNY",
    "INR",
    "TWD",
    "MXN",
    "CAD",
]

# STARTING BOT
bot = commands.Bot(command_prefix='$')
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])

bot.run(CONFIG["discord"])
