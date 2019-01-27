FROM debian:jessie
# COPY ./public-html/ /usr/local/apache2/htdocs/
# ADD ./public-html /usr/local/public-html/
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "apache2", "vim"]

ADD andy-yao.com.conf /etc/apache2/sites-available/
ADD andy-yao.com-le-ssl.conf /etc/apache2/sites-available/

VOLUME [ "/var/www/andy-yao.com/build"]

RUN chmod -R 755 /var/www
RUN a2ensite andy-yao.com.conf

# RUN service apache2 restart
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
