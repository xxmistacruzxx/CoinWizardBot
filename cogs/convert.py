import discord
from discord.ext import commands
from discord.commands import Option
import requests

from index import CONFIG
from index import EMBEDCOLOR
from index import DEVGUILDS
from index import CRYPTOCOMPARECOINCHOICES
from index import CRYPTOCOMPARECURRENCYCHOICES


class Convert(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="convert",
        description="Converts cryptocurrency amount to country currency value (default is BTC to USD).",
        guild_ids=DEVGUILDS,
    )
    async def convert(
        self,
        ctx: discord.ApplicationContext,
        amount: Option(
            float, "An amount of cryptocurrency to convert", required=True, min_value=0
        ),
        coin: Option(
            str,
            "A cryptocurrency type to convert from",
            required=True,
            choices=CRYPTOCOMPARECOINCHOICES,
            default="BTC",
        ),
        currency: Option(
            str,
            "A country currency type to convert to",
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
            title="{symbol1} to {symbol2}".format(symbol1=coin, symbol2=currency),
            color=EMBEDCOLOR,
        )
        embedVar.set_footer(
            text="Powered by CryptoCompare",
            icon_url="https://www.cryptocompare.com/media/20562/favicon.png",
        )
        try:
            raw = r.json()["RAW"][coin][currency]
            display = r.json()["DISPLAY"][coin][currency]
            currencyWorth = float(raw["PRICE"])
            value = str(currencyWorth * amount)
            embedVar.description = "{symbol1} {amount} = {symbol2} {value}".format(
                symbol1=display["FROMSYMBOL"],
                amount=amount,
                symbol2=display["TOSYMBOL"],
                value=value,
            )
        except Exception as e:
            embedVar.add_field(name="ERROR", value=str(e), inline=False)

        await ctx.respond(embed=embedVar)
        return


def setup(client):
    client.add_cog(Convert(client))
