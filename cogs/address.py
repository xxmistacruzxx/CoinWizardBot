import datetime
import discord
from discord.ext import commands
from discord.commands import Option
import requests

from index import CONFIG
from index import EMBEDCOLOR
from index import DEVGUILDS

ETHERSCANAPI = None
if "etherscan" in CONFIG:
    ETHERSCANAPI = CONFIG["etherscan"]


class Address(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="address",
        description="Gets info of a cryptocurrency address.",
        guild_ids=DEVGUILDS,
    )
    async def address(
        self,
        ctx : discord.ApplicationContext,
        coin: Option(
            str,
            "A type of crytocurrency in which the address is held",
            required=True,
            choices=["BTC", "ETH"],
        ),
        address: Option(str, "An address to lookup", required=True),
    ):
        embedVar = discord.Embed(
            title="{coin} Address Info".format(coin=coin),
            description="**Address:** {address}".format(address=address),
            color=EMBEDCOLOR,
        )

        match coin:
            case "BTC":
                # Send BTC Requests
                balanceR = requests.get(
                    "https://blockchain.info/q/addressbalance/{address}?confirmations=3".format(
                        address=address
                    )
                )
                receivedR = requests.get(
                    "https://blockchain.info/q/getreceivedbyaddress/{address}?confirmations=3".format(
                        address=address
                    )
                )
                sentR = requests.get(
                    "https://blockchain.info/q/getsentbyaddress/{address}?confirmations=3".format(
                        address=address
                    )
                )
                seenR = requests.get(
                    "https://blockchain.info/q/addressfirstseen/{address}".format(
                        address=address
                    )
                )
                # Construct BTC Embed
                embedVar.set_footer(
                    text="Powered by Blockchain API",
                    icon_url="https://pbs.twimg.com/profile_images/1268534114904391681/jXyihSx9_normal.png",
                )
                embedVar.add_field(
                    name="**__Balance__**",
                    value="BTC " + str(int(balanceR.text) / 10**8),
                    inline=False,
                )
                embedVar.add_field(
                    name="**__Total Received__**",
                    value="BTC " + str(int(receivedR.text) / 10**8),
                    inline=False,
                )
                embedVar.add_field(
                    name="**__Total Sent__**",
                    value="BTC " + str(int(sentR.text) / 10**8),
                    inline=False,
                )
                embedVar.add_field(
                    name="**__First Seen__**",
                    value=datetime.datetime.fromtimestamp(int(seenR.text)),
                    inline=False,
                )
            case "ETH":
                # Send ETH Requests
                balanceR = requests.get(
                    "https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api}".format(
                        address=address, api=ETHERSCANAPI
                    )
                )
                lastBlockR = requests.get(
                    "https://api.etherscan.io/api?module=account&action=getminedblocks&address={address}&blocktype=blocks&page=1&offset=1&apikey={api}".format(
                        address=address, api=ETHERSCANAPI
                    )
                ).json()
                # Construct ETH Embed
                embedVar.set_footer(
                    text="Powered by Etherscan API",
                    icon_url="https://pbs.twimg.com/profile_images/1296736608482283520/6mDtyT6V_normal.jpg",
                )
                embedVar.add_field(
                    name="**__Balance__**",
                    value="ETH " + str(int(balanceR.json()["result"]) / (10**18)),
                    inline=False,
                )
                embedVar.add_field(
                    name="**__Last Block Mined__**",
                    value="**• Block Number:** {blockNumber}\n**• Time Mined:** {timeStamp}\n**• Block Reward:** ETH {blockReward}".format(
                        blockNumber=lastBlockR["result"][0]["blockNumber"],
                        timeStamp=lastBlockR["result"][0]["timeStamp"],
                        blockReward=str(
                            int(lastBlockR["result"][0]["blockReward"]) / (10**18)
                        ),
                    ),
                    inline=False,
                )
            case _:
                ctx.respond("Failed to parse coin type. Please try again.")
                return

        await ctx.respond(embed=embedVar)
        return


def setup(client):
    client.add_cog(Address(client))
