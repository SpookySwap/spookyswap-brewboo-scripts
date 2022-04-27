# SpookySwap Sample BrewBoo Caller Script

## Overview
The BrewBoo v3 contract (https://ftmscan.com/address/0x3B3fdC40582a957206Aed119842F2313DE9eE21b) collects protocol fees from SpookySwap. It permissionlessly allows any party to call the contract  convert the collected protocol fees to BOO, which is then sent to xBOO. Callers will receive a 0.1% bounty for calling the contract.

The python3 script provided in this repo is an example of calling BrewBoo v2.

## Setup
This setup assumes python3 and pip3 are available.

1. Clone the repo
```
git clone https://github.com/SpookySwap/spookyswap-brewboo-scripts.git
```

2. Navigate to the repo and install the python3 requirements
```
pip3 install -r requirements.txt
```

3. With your favorite text editor, create a `.env` file to store a wallet's hex private key.
Example of expected contents for the `.env` file:
```
PRIVATE_KEY=4bd1283169c03c542276521992b85c5e17cab72e6ee702e1dbfc687f16327d33
```

**IMPORTANT:** This is not a real private key. Never reveal your private key to anyone. Compromising your private key compromises all control and funds in the respective wallet. DO NOT CHECK THIS FILE IN ANYWHERE. The `.gitignore` of this repo has `.env` included. It is not recommended to change this.

4. Edit the `brewBoo.py` script's token pairs to choose which pairs to convert. BrewBoo v3's value can be tracked with https://debank.com/profile/0x3b3fdc40582a957206aed119842f2313de9ee21b

Note: DeBank does not always include newly minted tokens. The analytics page can help find these pairs.

5. Call the script and follow the prompts.
Sample call:
```
python3 brewBoo.py
You have some FTM to perform encantations.
Continue? (y/n)
y
Type: 'BrewBoo' to activate the Brewing ritual
BrewBoo
Successful Brew!

Continue the Brew to create BOOs? (y/n)
y
As you wish, brewing BOOs to complete ritual...
```
