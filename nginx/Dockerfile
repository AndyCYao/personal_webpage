FROM nginx:latest
# COPY ./public-html/ /usr/local/apache2/htdocs/
# ADD ./public-html /usr/local/public-html/
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
ADD default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/andy-yao.com/build
# ADD andy-yao.com.conf /etc/apache2/sites-available/
# ADD andy-yao.com-le-ssl.conf /etc/apache2/sites-available/

# RUN chmod -R 755 /var/www
# RUN a2ensite andy-yao.com.conf

# RUN service apache2 restart
# CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
