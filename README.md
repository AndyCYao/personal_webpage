# Andy's Personal Webpage

This is the source code for my personal webpage. This is a site built with pelican. Follow this quick start https://docs.getpelican.com/en/stable/quickstart.html


## Initial Set up

### Nginx Set up
- copy the nginx/default.conf into `/etc/nginx/sites-available/` , then link it to
`sites-enabled` using `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/`
- check if things are right with `nginx -t`


### Pelican Set up
- navigate to andy-yao.com/, and run `pelican -t gum`, this applys the `gum` theme to the webpage

## General Workflow
- write your blog content under andy-yao.com/content
- use `pelican content` to build the content into `output` folder
- use `pelican --listen` to check out your website on localhost:80
- run `make upload` to deploy the website


docker run -it --rm \
      -v certs:/etc/letsencrypt \
      -v certs-data:/data/letsencrypt \
      deliverous/certbot \
      certonly \
      --webroot --webroot-path=/data/letsencrypt \
      -d andy-yao.com -d www.andy-yao.com

## Todo:
- make nginx a dedicated process in lightsail, instead of docker
- install HTTPS on lightsail.