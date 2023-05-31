# Introduction
CoinWizardBot is a Discord Bot designed to bring cryptocurrency related slash commands to Discord.

# Commands
Parameters surrounded with "< >" are required, while "[ ]" are optional. 
## /address \<coin\> \<address\>
Gets info of a cryptocurrency address.<br>
    • coin: A cryptocurrency to get market data of | options: BTC, ETH<br>
    • address: An address to lookup<br>

## /convert \<amount\> \[coin\] \[currency\]
Converts cryptocurrency amount to country currency value (default is BTC to USD).<br>
    • amount: An amount of cryptocurrency to convert<br>
    • coin: A cryptocurrency type to convert from - default is BTC<br>
    • currency: A country currency type to convert to - default is USD<br>

## /market \[coin\] \[currency\]
Gives basic market info about a given cryptocurrency (default is BTC, shown in USD).<br>
    • coin: A cryptocurrency to get market data of - default is BTC<br>
    • currency: A country currency to compare the worth of the cryptocurrency to - default is USD<br>

# APIs, Tools, & Libraries Used
## Libraries
• [discord.py](https://discordpy.readthedocs.io/en/stable/index.html)<br>
• [py-cord](https://docs.pycord.dev/en/stable/index.html)<br>
• [requests](https://pypi.org/project/requests/)<br>
## APIs
• [CryptoCompare API](https://min-api.cryptocompare.com/documentation)<br>
• [Blockchain API](https://www.blockchain.com/explorer/api)<br>
• [Etherscan API](https://docs.etherscan.io/)<br>