title: How does files get broken up in packets when transfer over
date: 2018-09-18
summary: File Transfer Protocol And Bit Torrent
image: 
published: true

__File Transfer Protocol (FTP)__ is an application layer (Layer 7 in OSI) protocol used for file transfers. It uses TCP underneath for orderly transfers. 

FTP sends files one at a time in the form of data streams, and then it closes connection afterwards. 

__Bit Torrent__ is a Peer 2 Peer protocol, files are downloaded in chunks owned by various peers in the network. 

