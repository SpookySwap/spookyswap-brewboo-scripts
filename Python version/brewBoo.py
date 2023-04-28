from dotenv import dotenv_values
from web3 import Web3
import spookyswap_tokens as tokens

token0 = []
token1 = []

# Tokens paired with FTM, USDC/FTM, fUSDT/FTM, etc
FTM_PAIRS = [
  # ADD OR REMOVE TOKENS HERE.
  tokens.USDC,
  tokens.fUSDT,
  tokens.DAI,
  tokens.TREEB,
  tokens.MULTI,
  tokens.ANY,
  tokens.BIFI,
  tokens.GEIST,
  tokens.BOO,
]

# DAI pairs. Popular with OHM forks
DAI_PAIRS = [
  # ADD OR REMOVE TOKENS HERE.
  tokens.USDC,
]

#LPamounts LPamounts should be set to the brewboo contract LP token balance (in wei) for each LP token pair you are buying back.
#If you want to use the old functionality that buys back the current balance, you can pass [] (empty array) for LPamounts
LPamounts =[
  #contract LP token balance(wei) 
]

for token in FTM_PAIRS:
  token0.append(tokens.FTM)
  token1.append(token)

for token in DAI_PAIRS:
  token0.append(tokens.DAI)
  token1.append(token)

# Custom pairs

# Example for adding USDC/OXD and BTC/ETH
token0.append(tokens.USDC)
token1.append(tokens.OXD)

token0.append(tokens.BTC)
token1.append(tokens.ETH)

assert len(token0) == len(token1)

config = dotenv_values(".env")
privateKey = config["PRIVATE_KEY"]

BREWBOO_ABI ='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_xboo","type":"address"},{"internalType":"address","name":"_boo","type":"address"},{"internalType":"address","name":"_wftm","type":"address"},{"internalType":"address","name":"route1","type":"address"},{"internalType":"address","name":"route2","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"bridge","type":"address"}],"name":"LogBridgeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"server","type":"address"},{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountBOO","type":"uint256"}],"name":"LogConvert","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_adr","type":"address"}],"name":"LogSlippageOverrode","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_adr","type":"address"}],"name":"LogToggleOverrode","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_addr","type":"address"}],"name":"SetDevAddr","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"SetDevCut","type":"event"},{"inputs":[],"name":"BOUNTY_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_auth","type":"address"}],"name":"addAuth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"authorized","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bridgeRoute","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bridgeRouteAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"token0","type":"address[]"},{"internalType":"address[]","name":"token1","type":"address[]"},{"internalType":"uint256[]","name":"LPamounts","type":"uint256[]"}],"name":"convertMultiple","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devAddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"devCut","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract IUniswapV2Factory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isAuth","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastRoute","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"tokens","type":"address[]"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"overrideSlippage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"overrode","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"pairOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_auth","type":"address"}],"name":"revokeAuth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"bridge","type":"address"}],"name":"setBridge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"address","name":"token","type":"address"}],"name":"setBridgeRoute","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setBridgeRouteAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"setDevAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setDevCut","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"setSlippage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapper","outputs":[{"internalType":"contract ISwapper","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"swapperApproved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"xboo","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
BREWBOO_ADDRESS = "0x3B3fdC40582a957206Aed119842F2313DE9eE21b"

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/fantom"))

brewBoo = w3.eth.contract(address=BREWBOO_ADDRESS, abi=BREWBOO_ABI)
w3.eth.default_account = w3.eth.account.privateKeyToAccount(privateKey).address
ftm_balance = w3.fromWei(w3.eth.get_balance(w3.eth.default_account), 'ether')

string = input(f"You have some FTM to perform incantations.\r\nContinue? (y/n)\r\n")

if string.lower() != "y":
    print("Dissolving preparations...")
    exit()

nonce = w3.eth.get_transaction_count(w3.eth.default_account)
result = brewBoo.functions.convertMultiple(
    token0,
    token1,
    LPamounts
).buildTransaction({
    'chainId': 250,
    'gas': 9000000,
    'gasPrice': w3.eth.gas_price,
    'nonce': nonce,
})

string = input("Type: \'BrewBoo\' to activate the Brewing ritual\r\n")

if string != "BrewBoo":
    print("Brew failed!")
    exit()

print("Successful Brew!\r\n")

string = input("Continue the Brew to create BOOs? (y/n)\r\n")

if string.lower() != "y":
    print("Brew halted, completing the ritual.")
    exit()

print("As you wish, brewing BOOs to complete ritual...")

signed_tx = w3.eth.account.sign_transaction(result, private_key=privateKey)

w3.eth.send_raw_transaction(signed_tx.rawTransaction)
result = w3.toHex(w3.keccak(signed_tx.rawTransaction))
print(f"https://ftmscan.com/tx/{result}")
print(f"https://dashboard.tenderly.co/tx/fantom/{result}")
