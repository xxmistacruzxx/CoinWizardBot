import discord
from discord.ext import commands
from discord.commands import Option
import requests

from index import CONFIG
from index import EMBEDCOLOR
from index import DEVGUILDS
from index import CRYPTOCOMPARECOINCHOICES
from index import CRYPTOCOMPARECURRENCYCHOICES

CRYPTOCOMPAREAPI = None
if "cryptocompare" in CONFIG:
    CRYPTOCOMPAREAPI = CONFIG["cryptocompare"]


class Market(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="market",
        description="Gets basic market info of a cryptocurrency (default is BTC, shown in USD).",
        guild_ids=DEVGUILDS,
    )
    async def market(
        self,
        ctx : discord.ApplicationContext,
        coin: Option(
            str,
            "A cryptocurrency to get market data of",
            required=True,
            choices=CRYPTOCOMPARECOINCHOICES,
            default="BTC",
        ),
        currency: Option(
            str,
            "A country currency to compare the worth of the cryptocurrency to",
            choices=CRYPTOCOMPARECURRENCYCHOICES,
            required=True,
            default="USD",
        ),
    ):
        r = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={coin}&tsyms={currency}".format(
                coin=coin, currency=currency
            )
        )
        embedVar = discord.Embed(
            title="{symbol} Market Info".format(symbol=coin),
            color=EMBEDCOLOR,
        )
        embedVar.set_footer(
            text="Powered by CryptoCompare",
            icon_url="https://www.cryptocompare.com/media/20562/favicon.png",
        )

        try:
            raw = r.json()["RAW"][coin][currency]
            display = r.json()["DISPLAY"][coin][currency]
        except Exception as e:
            embedVar.add_field(name="ERROR", value=str(e), inline=False)
            await ctx.respond(embed=embedVar)
            return

        embedVar.set_thumbnail(
            url="https://www.cryptocompare.com/{url}".format(url=raw["IMAGEURL"])
        )
        embedVar.description = (
            "**• Supply:** {supply}\n**• Market Capitalization:** {mktcap}".format(
                supply=display["SUPPLY"], mktcap=display["MKTCAP"]
            )
        )
        changeh = "{value} ({percentage}%)".format(
            value=display["CHANGEHOUR"], percentage=display["CHANGEPCTHOUR"]
        )
        change24h = "{value} ({percentage}%)".format(
            value=display["CHANGE24HOUR"], percentage=display["CHANGEPCT24HOUR"]
        )
        embedVar.add_field(
            name="**__Price__**",
            value="**• Current:** {currprice}\n**• Open of 24h:** {openday}\n**• High of 24h:** {highday}\n**• Low of 24h:** {lowday}\n\n**• Change 1h:** {changeh}\n**• Change 24h:** {change24h}".format(
                currprice=display["PRICE"],
                openday=display["OPEN24HOUR"],
                highday=display["HIGH24HOUR"],
                lowday=display["LOW24HOUR"],
                changeh=changeh,
                change24h=change24h,
            ),
            inline=False,
        )
        embedVar.add_field(
            name="**__Volume__**",
            value="**• Volume Traded 1h:** {volume1h} ({volume1hto})\n**• Volume Traded 24h:** {volume24h} ({volume24hto})".format(
                volume1h=display["VOLUMEHOUR"],
                volume1hto=display["VOLUMEHOURTO"],
                volume24h=display["VOLUME24HOUR"],
                volume24hto=display["VOLUME24HOURTO"],
            ),
            inline=False,
        )

        await ctx.respond(embed=embedVar)
        return


def setup(client):
    client.add_cog(Market(client))
