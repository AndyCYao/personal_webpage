# Andy's Personal Webpage

This is the source code for my personal webpage. This is a pelican built website. Follow this quick start https://docs.getpelican.com/en/stable/quickstart.html


## How to configure

install venv with `python3 -m venv /path/to/new/virtual/environment`

Create a new folder call `private` in the main level

Create two files in this folder.

`config.ini`, `RSA key`

the config.ini file is where blog.py looks for the configurations

    [server]
    user = xxx
    path = xxx-west-2.compute.amazonaws.com
    folder = /var/xxx

    [other]
    key = private/RSA Key

## Set up 
The blog.py lets you do 3 things

`python blog.py` runs the website in your local address, lets you debug.   

`python blog.py build` builds the static website using Python Flask's `freeze`. The website is stored in the `build` folder.

`python blog.py deploy` deploys the website based on the configurations earlier.
