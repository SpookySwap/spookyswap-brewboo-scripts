from dotenv import dotenv_values
from web3 import Web3
import spookyswap_tokens as tokens

token0 = []
token1 = []

# Tokens paired with FTM, USDC/FTM, fUSDT/FTM, etc
FTM_PAIRS = [
  # ADD OR REMOVE TOKENS HERE.
  tokens.USDC,
  tokens.TOMB,
  tokens.TSHARE,
  tokens.fUSDT,
  tokens.DAI,
  tokens._3SHARES,
  tokens._2OMB,
  tokens.IB,
  tokens.SPELL,
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

BREWBOO_ABI = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_bar","type":"address"},{"internalType":"address","name":"_sushi","type":"address"},{"internalType":"address","name":"_weth","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"bridge","type":"address"}],"name":"LogBridgeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"server","type":"address"},{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountSUSHI","type":"uint256"}],"name":"LogConvert","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"bar","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"bridgeFor","outputs":[{"internalType":"address","name":"bridge","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"}],"name":"convert","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"token0","type":"address[]"},{"internalType":"address[]","name":"token1","type":"address[]"}],"name":"convertMultiple","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract IUniswapV2Factory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"bridge","type":"address"}],"name":"setBridge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"},{"internalType":"bool","name":"direct","type":"bool"},{"internalType":"bool","name":"renounce","type":"bool"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
BREWBOO_ADDRESS = "0x68f598280a843A5Ce07C1b9fB0D3aF00Cd085c31"

w3 = Web3(Web3.HTTPProvider("https://rpc.ftm.tools"))

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
    token1
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