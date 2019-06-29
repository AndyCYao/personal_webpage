#!/usr/bin/bash
# follow this article to set up certbot https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:certbot/certbot -y
sudo apt-get update -y
sudo apt-get install certbot -y

