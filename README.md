# Andy's Personal Webpage

This is the source code for my personal webpage. This is a site built with pelican. Follow this quick start https://docs.getpelican.com/en/stable/quickstart.html


## Initial Set up
- Create your docker machine, I am using a docker-machine on EC2
- set the machine with `eval $(docker-machine env X)`
- in the root folder, run `docker-compose up --build -d` to build the nginx container
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