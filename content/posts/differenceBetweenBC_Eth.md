title: What is the difference between ethereum trade and bitcoin trade
date: 2018-09-06
published: true
summary: bitcoin and ethereum accounting differences

I was asked this question during an interview, and I couldn't answer it. Well I have researched it and here is the answer.

--- 

The context is

`how would we track a bitcoin's transaction to see if a wallet is a money launderer?`

Below is taken from [ethereum design rational](https://github.com/ethereum/wiki/wiki/Design-Rationale#accounts-and-not-utxos).
## Bitcoin 
- Bitcoin balance are tracked by unspent transaction outputs (UTXO), think each UTXO as a coins like nickle, penny, dimes.
- each `UTXO coin` has to have a value, and an owner. 
    * this has a high degree of privacy, users can use a new address for each transaction they receive, and will be difficult to link to each other. 
- _A user's balance in the system is the total value of the set of coins for which the user has a private key capable of producing a valid signature_
- Bitcoin Blockchain has limit of 1MB. so there is a finite # of transaction to fit in a block.

on blockchain.com, we see that every wallet's transaction is recorded publicaly.

!["This is our result after two weeks"](/static/images/blockchain.png)

## Ethereum
- Ethereum the global state stores a list of accounts, with balance, codes and internal storage. 
- the balance is represented by a `uint` number. 
    * this means ethereum tokens are more `fungible`.
- Ethereum blockchain has no blocklimit, # of transaction in a block is decided by the miner. 