# Andy's Personal Webpage

This is the source code for my personal webpage. This is a site built with pelican. Follow this quick start https://docs.getpelican.com/en/stable/quickstart.html


## Initial Set up
- Create your docker machine, I am using a docker-machine on EC2
- set the machine with `eval $(docker-machine env X)`
- in the root folder, run `docker-compose up --build -d` to build the apache container
- navigate to andy-yao.com/, and run `pelican -t gum`

## General Workflow
- write your blog content under andy-yao.com/content
- use `pelican content` to build the content into `output` folder
- run `make ssh_upload` to deploy the website
