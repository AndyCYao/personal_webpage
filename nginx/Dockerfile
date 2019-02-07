FROM nginx:latest

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

RUN ["add-apt-repository", "ppa:certbot/certbot"]
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "python-certbot-nginx"]

ADD default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/andy-yao.com/build
# RUN ["certbot", "--nginx", "-d", "andy-yao.com", "-d", "www.andy-yao.com"]
EXPOSE 80 443
# follow this for certbox openSSL 
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04