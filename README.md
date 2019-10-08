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
- run `make upload` to deploy the website
- run `pelican --debug --listen --autoreload` to check the website locally

## Website Todo:
- Done. make nginx a dedicated process in lightsail, instead of docker
- Done. install HTTPS on lightsail.
- Done. modify the pelican's `make upload` to FTP or SCP the files into lightsail's /var/www/andy-yao
- Done add an unpublish flag to each article? or other ways to prevent course notes from coming

## Content Todos:
- get correct formula lexing for school notes
- update About
- add github photo

