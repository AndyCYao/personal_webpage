title: IPFS Notes
date: 2018-09-10
summary: IPFS shortcuts, commands, concepts
image: 
published: true

### Key Commands
`ipfs init` to start the local node

`ipfs add fileX` hashs fileX, and returns an address of the file. The address is based on the content of the file. so its deterministic

`ipfs cat HashOfFileX` returns the content of the file

`ipfs daemon` to take things online, which creates the API server, and Gateway server

### Commands for Docker Container of IPFS
source https://hub.docker.com/r/jbenet/go-ipfs/

### IPFS Concepts
`ipfs` trys to make every object local. so `ipfs pin` will cache an object locally for fast access. `ipfs add` pins object by default.

`ipfs swarm peers` to see the peers you are connect to 

`DHT` is distributed hash table