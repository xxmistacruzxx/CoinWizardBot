# Introduction
CoinWizardBot is a Discord Bot designed to bring cryptocurrency related slash commands to Discord.

# Commands
## /address \<coin\> \<address\>
Gets info of a cryptocurrency address.
    • coin: A cryptocurrency to get market data of | options: BTC, ETH
    • address: An address to lookup

## /convert \<amount\> \[coin\] \[currency\]
Converts cryptocurrency amount to country currency value (default is BTC to USD).
    • amount: An amount of cryptocurrency to convert
    • coin: A cryptocurrency type to convert from - default is BTC
    • currency: A country currency type to convert to - default is USD

## /market \[coin\] \[currency\]
Gives basic market info about a given cryptocurrency (default is BTC, shown in USD).
    • coin: A cryptocurrency to get market data of - default is BTC 
    • currency: A country currency to compare the worth of the cryptocurrency to - default is USD

# APIs, Tools, & Libraries Used
## Libraries
• Discord.py
• py-cord
• requests
## APIs
• [CryptoCompare API](https://min-api.cryptocompare.com/documentation)
• [Blockchain API](https://www.blockchain.com/explorer/api)
• [Etherscan API](https://docs.etherscan.io/)