title: "Blockchain Development"
date: 2018-08-11
semester: "Summer 2018"
code: "blockchain"

### Notes from 7Gate Blockchain Bootcamp Aug - Sept 2018

---
### Jul 31st 2018
ethernet addresses are public

etherscan.io lets you see accounts, transactions. 

ethgasstation.info looks at what “gas” are in units of ethernet “gwel”.  the higher this is , the faster the transaction will be in the block. 

Best Practice for generating wallet
- download ethereum
- create new wallet offline

Metamask
needed to access the distributed applications.

Open Bazaar
https://openbazaar.org/
is like craigslist, but uses metamask 

---

### Aug 1st 2018
Reza CTO Of CoinField
Hashing Algorithm
- SHA256 is the main hashing function for bitcoin
- a 64 char hexadecimal string

Hashing algorithms must follow
- One way
- Deterministic, everytime you hash a file, it always gets the same hash back. so idempotent.  
- Fast Computation -> must be able to validate quickly
- Avalanche Effect -> any change in the file must generate new hash. 
- Must Withstand collision.

A nonce is an arbitrary number used just once, to get different hash every try

every two week all client decide the target number gets smaller.  as in there are more leading zeros 

read more at en.bitcoin.it/wiki/Difficulty

moonGo is a crypto currency credit card. (sponsor by Reza’s company coinfield)

Miners
Mining Rigs such as asic, machines. 

Mining pools will work as a team to solve hash. AntPool, BTCC Pool, TC> Top, ViaBTC.  s9 ant miner which are designed specifically for SHA 256
 

miner has a memory pool, all transaction are  queued up in the memory pool, and miners decide which transaction to include. 

When all the bitcoins are mined, then proof of work changes to proof of stake so that miners have an incentive to keep processing the transaction. 

Consensus Protocol - 

Proof of Work (bitcoin,.) -> means miner has spend money and time to get the work, so we should trust them.  miners compete to add the next block. racing to solve 
Proof of activity (ethereal), -> means when you done mining then u go to proof of stake
Proof of Stake ( Dash) -> means we trust someone by seeing how much assets he is putting as a stake. the higher their stake, the more probable they will win the process. 
Proof of Burn  -> miners would burn or send funds to a irrecoverable address. 
Proof of Capacity -> capacity 
Proof of elapsed time (intel)

If two miners both solves the hash, and broadcast at the same time to the network, the one with more connect nodes would 

there is financial incentive to play by the rule, cheating is not worth it because amount of electricity consumed by mining, 

en.bitcoin.it/wiki/protocol_rules

Blockchain Weaknesses
majority attack (51% attack) - if a malicious actor becomes 51% of the network, they control what the blockchain is.

main in the middle attack - i am a miner, and i found a correct hash, when i broadcast, and a malicious person gets my answer , then the attacker can distortion

double spend attack - I’m a hacker with a number of nodes. i confirm a transaction through these node

Hacker A sends 5 coins through a controlled node to B , which are “fake” transaction
the exchange assumes its true, and grants 5 coins back, 
but in 10 minutes, the blockchain is updated and the exchange is lost. 

in Reza’s CoinField, the bitcoin gold had double spent attack. so what they do to mitigate this is to wait for high number of confirmations before they grant money. 

---

### Aug 2nd 2018

Block Headers
- includes version name
- previous block header hash
- SHA 256 hash of all the transaction ID in this block (merkle root hash)
- time
- target nBits, 
- nonce , 

Bitcoin-cli is the main entry point for a server

json rpc calls 

Forks
- used for rule changes, when a fork happen all nodes either need to go with the old branch all the new branch. 
- soft forks are backward compatitible

Bitcoin-CLI
do 
testnet = 1 
in the .bitcoin/bitcoin[sp]?.conf  to start testing 



Open Discussion:
- Scalability issues?
    - there are weaknesses in bitcoin , like if the blocksize increase, then data needed increases. and the number of miners decreases because its hard to scale.
    - 
- what happens if nobody mines
- blockchain control (massive mining pools)
    - augur contract 

--- 

### Aug 3rd 2018

Whisper and IPFS. 
Whisper is like decentralize web socket. 

Whisper can be used for plausible deniability, 

there are such things as bitcoin tumbler -> which is for laundering bitcoin between two wallet. 

geth is ethereum’s version of bitcoin-cli

IPFS
HTTP is location address

IPFS is content address -> it would ask the hash of a file, then it will return the content of the file. 
this is based on kademila (DHT) + Bit torrent + Git

Learn about merkel DAG and merkel Tree

---

### Aug 7th, 8th  2018

Public Key Encryption
We learned about RSA, Diffie-Hellman, and Elliptic Curve public key algorithm.

![diffie-hellman]({static}/images/diffie-hellman-key-exchange.png)

- server session key , and various vulnerabilities such as man in middle. 
- zero knowledge proof, with analogy in the alibaba cave


### Aug 9th 2018 Diffie Hellman Key Generation
Conference Protocol

Forward Secrecy key exchange
ie don’t let jimmy know we change date of the party, forward secrecy means jimmy will not be able to find out the change. 

Backward Secrecy Key exchange
i.e. don’t let mom know we had this party, backward secrecy means mom will not be able to find out 

burmester desmedt protocol
 
----

### Aug 11 2018 Saturday William Phan

#### Bitcoin UTXO model

- Bitcoin Review. 
- UTXO - think like nickels, dimes , change in account value 
- input of transactions have to equal to output of transaction like a ledger
    - so if Alice has 1 btc. and she sends bob .8 btc. then there is a .2 btc created to balance 
- bitcoin is a transaction base state machine. 
- the in and out in transaction refers to the UTXOs going in and out. 
- Satoshi is a unit of bitcoin to the 18th place. 
- bitcoin “dust” means UTXOs that are so small people can’t do anything with it. because we can’t split UTXO, just create new UTXOs

bitcoin script is Stack based , read from left to right, but not turing complete (so no loops, jumps) , bitcoin script can’t access the state of the bitcoin. 


#### Data Structures In Ethereum.

-dont handle in UTXO, each account balance is a long integer. 

Recursive Length Prefix (RLP), this is a serialization format for data. 

Merkle Trees  splitting data in chunks and storing in buckets. hash of buckets stored in a tree structure. 

in bit torrent, merkel tree root is the file you are downloading. 

ethereum uses Merkel Patricia Trie to implement key value store , and offer cryptographic guaranteeds. 

the root of the tree are stored in the blockchain, but the miner keeps the whole tree structure. 

Bloom Filters IMPORTANT . 
    - probabilistic data structure. 
    - 

Ethereum DApps.
    - has the most developers working on it. 

any of the new coins are just ethereum smart contracts. 

__Ethereum Virtual Machine (EVM)__ every full node runs an EVM 

Gas = StartGas - 5 * len(DATA) (subtract 5 gas per byte in txt data)


#### Smart Contract

You can think of smart contract as "objects" in OOP. one of the Op code in ethereum is "delegate call", which allows you to reference other smart contracts. 

You can look for smart contract library by looking for main net address. 

The main programming langauge for smart contract is __solidity__ , is contract oriented, has inheritance, has inline assembly. 

as smart contract developers, we dont get to control the order of execution in the block. that's up to the miner. 

if a smart contract is design like functional programming, as in it doesn't modify any state, then this does not have to be commit to the block , so saves on gas. 

--- 
### Aug 14 2018 Monday William Phan
EVM is deterministic, so it is hard to get randomness in the system. 

Look into profitTrailer

---
### Aug 15 2018 Tuesday William Phan
To check if a public address is a smart contract instead of a real perosn , check the code field of the transaction. 

counterparty risk - a chance that the person might not uphold the contract, 

oraclized - allows randomize mechanism

__ERC 721__ proposes a creation of non-fungible units, like cryptokitty


--- 
### Aug 16 2018 

* Layer 1 - requires global consensus, ethereum, bitcoin etc.
    
* Layer 2 systems are "off chain",  builds off of on chain Layer 1 , like Lightning network, Raiden,
    - Lightning network allows everyone to send money to each other, as long as they are in the same network. 
    - but miners gain nothing from payment channels adoption
    - lightning node may be considered by FinCEN as a money transmitter


3 Scaling solution - 

1. centralize database (coin base, credit card payment processor) 
    - custodial risk
    - con  custodial risk.

2. payment channcel (starbucks giftcard model)
    - need to have channel open by both party
    

3. sidechains
    - creating blockchain ontop of blockchain. 
    - Loom network -> no ICO, no whitepaper. 



Guest Speaker Today - Mimik - Decentralize Cloud. 
    Faye Arjamandi - 
    
- turn cloud by adding processing from the devices level. 
- lots of surplus processing from devices unused. 
- end to end SDK kit, use it to develop applications 

---
### Aug 17th 2018 - Privacy
zkSNARKS -> zero knowledge proofs

ring signature -> masks senders address. 

Byzantium block means any after blcok has EVM byte codes precompiled. 

ethereum supports zkSNARKS things. 

Two main competitors right now in private coins, `ZCash` which uses zkSnark and `Monero` which uses ring signatures to mask signature address.




Segegrated networks for bitcoin allows for lightning networks. 

---
### Aug 20th 2018 - Vincent
1. Run your company before you run a token

#### Ethernaut Solidity Tips

* `GetBalance(address)` returns the balance of the contract.
* `contract.sendTransaction()` sends ethers to a contract
* `contract.abi` to see the list of available functions for the contract
* `web3.sha3(methodname)` to get the address of the method
* solidity currently does not enforce view and constant and pure functions to not modify state. So they should not read state but they can. 

### Aug 21st 2018 - Vincent
__Token Economics__

there are 3 types of tokens

1. Currencies / Commodities
    - Storer of value, stable coins, like bitcoin
2. Utility Token
    - coupons, governance tokens, work tokens
3. Security Token
    - considered securities, so may have regulations, anything that provides dividend. Zook coin. 

Questions to ask about token mechanic. 
1. what is the purpose
2. how will the token assist the project infrastructure
3. who is using the token, 
4. who is holding the token to support the network.
5. does the token grant governance action. 
6. is this used to raise capital from investors?

__Token velocity__

Velocity = Total Transaction Volume / Average Network Value

_DCTRL community commons:_

### Aug 22nd 2018 - Vincent

Some current blockchain projects include 

sliver.tv , stream with betting element using proprietary `theta` token. 

dappradar.com , checks the ethereum usage 

### Aug 23rd 2018 - Reza Dehghani

Binance and Bitfinex are centralized exchanges. Quadriga deals in canadian dollars. 

`Forwards` are contracts that never expires. 

`CoinSchedule` gives ICO schedules 

limit orders are 0.25% per trade. in bitmex

BTC Futures 

WhalesWisdom.com

TA - Lib  colabratory 

TradingView as back testing using the pine test

`Catalyst` - > BTC Python algo trading

`Zipline` -> python Quantopia framework 

### Aug 24th 2018 - Reza Dehghani

you can look at the CME bitcoin futures to see the volume of long and short futures. The bigger the volume, the more likely bitcoin will go for that direction. 


### Hyperledger
- open sourced community to build blockchain related usecases. 
- permissioned ledger system (as opposed to bitcoin / ethereum is public.) Transaction processing is done by predefined users.
- diff. than ethereum because hyperledger is more personalize per industry. whereas ethereum runs a general code.
- runs a consensus algorithm call "Practical Byzantine Fault Tolerance", new block is dadded when 2/3 of all validating peers submit the same response. 
There are a few roles in a hyper ledger
1. Committer 
    * appends validated transaction to their specific ledger

2. Endorser - a type of peer
    * Simulating transaction
    * verifies that transactions are correct

3. Consenter
    * network consesus service, decides if a transaction should be added to a ledger. 



#### Ethereum Notes:
1 ETH 

1E-9 GWei

1E-18 Wei


Questions to ask
- what happens to the peers that have different last hash than the majority, do they stay separated forever. 
		node has to be resync and may take several hours. 
- bitcoin improvement protocols (BIP). 
- What is ERC 20 - a protocol that new coins are built out of, to comply with ethereum
- Byzantine Princesses. 

Blockchain debt collector 

Requirement for building blockchain app
- the product has to solve something current solutions isn’t solving.
- the users can’t expect solutions to be instantaneous, since blockchain can’t resolve things as fast as say visa/mastercard
- (a) inter-company audit trails, (b) provenance tracking, and (c) lightweight financial systems. 
- ERC 20 tokens 

Ideas
- Maersk announced a blockchain based bill of lading proof of concept.
- Augur prediction helper using data from sports betting sites.
- ping smart contracts every 256 blocks, to make sure they are still active. 
- solidity gas calculator in every smart contract during code building. 
- Raiden raspberry pi lightning network. (using lighting protocol)


TA - Lib - Technical analysis for python 
