//libraries
const Web3 = require('web3');   //web3 library
require('dotenv').config() // Load .env variables


//variables
const tokens = require('./token-list.json'); //token list
const BREWBOO_ABI = require('./BrewBoo_ABI.json'); //BrewBoo ABI
const BREWBOO_ADDRESS = "0x3B3fdC40582a957206Aed119842F2313DE9eE21b" //BrewBoo address

//  add custom tokens, *is mandatory to add at least one token pair
var token0 = [tokens.MUMMY];
var token1 = [tokens.FTM];

//FANTOM PAIRS *Optional
const FTM_PAIRS = [
  // ADD OR REMOVE TOKENS HERE.
  tokens.DAI,
  tokens.BNB,
  tokens.fUSDT,
]

const ftmToken0 = Array(FTM_PAIRS.length).fill(tokens.FTM);
const ftmToken1 = FTM_PAIRS.map(pair => pair);

token0.push(...ftmToken0);
token1.push(...ftmToken1);

//DAI PAIRS *Optional. Popular with OHM forks
const DAI_PAIRS = [
  // ADD OR REMOVE TOKENS HERE.
  tokens.USDC,
]

const daiToken0 = Array(DAI_PAIRS.length).fill(tokens.DAI);
const daiToken1 = DAI_PAIRS.map(pair => pair);

token0.push(...daiToken0);
token1.push(...daiToken1);


(token0.length == token1.length) ? console.log("token0 and token1 are the same length") : (console.log("token0 and token1 are not the same length", process.exit()));

//RPC configuration
const w3 = new Web3("https://rpc.ankr.com/fantom")

//contract Call
const contractCall = async () => {
  const account = process.env.ADDRESS;
  const privateKey = process.env.PRIVATE_KEY;
  const contractAddress = BREWBOO_ADDRESS

  //init contract
  const brewBoo = new w3.eth.Contract(BREWBOO_ABI, BREWBOO_ADDRESS)

  // get nonce
  const transactionCount = await w3.eth.getTransactionCount(account);
  //console.log(transactionCount);

  // //get balance
  // const balance = await w3.eth.getBalance(account);
  // //console.log(balance);

  //get gasPrice
  const gasPriceWei = await w3.eth.getGasPrice();
  //const gasPriceFTM = w3.utils.fromWei(gasPriceWei,"ether")
  //console.log(gasPriceWei+" wei");
  //console.log(gasPriceFTM +" FTMs");

  //LPamounts LPamounts should be set to the brewboo contract LP token balance (in wei) for each LP token pair you are buying back.
  //If you want to use the old functionality that buys back the current balance, you can pass [] (empty array) for LPamounts
  const LPamounts = [
    //Contract LP token balance(wei) 
  ]

  //build BrewBOO call
  const data = await brewBoo.methods.convertMultiple(
    token0,
    token1,
    LPamounts
  ).encodeABI()
  //console.log(data);


  //build transaction 
  const txOptions = {
    "from": account,
    "to": contractAddress,
    "data": data,
    "value": 0,
    "gasPrice": gasPriceWei,
    "gas": 9000000,
    "nonce": transactionCount
  }
  //console.log(txOptions);

  //sign transaction
  signed_tx = await w3.eth.accounts.signTransaction(txOptions, privateKey)
  //console.log(signed_tx);

  //send transaction
  w3.eth.sendSignedTransaction(signed_tx.rawTransaction)
  console.log(`https://ftmscan.com/tx/${signed_tx.transactionHash}`)

  return 0;




}
contractCall(); // call the function to execute the transaction.


