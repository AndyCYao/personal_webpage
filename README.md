# Andy's Personal Webpage

This is the source code for my personal webpage. This is a site built with pelican. Follow this quick start https://docs.getpelican.com/en/stable/quickstart.html

## Initial Set up

### Pelican Set up
- navigate to andy-yao.com/, and run `pelican -t ../pelican-blue`, this applys the `pelican-blue` theme to the webpage

## General Workflow
- write your blog content under andy-yao.com/content
- use `pelican content` to build the content into `output` folder
~- run `make upload` to deploy the website~ now done with netlify, just push to master branch and netlify automatically builds
- run `pelican --debug --listen --autoreload` to check the website locally

