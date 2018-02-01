# Andy's Personal Webpage
This is the source code for my personal webpage. I followed [this post](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/) for the guideline. 

## How to configurate
Create a new folder call `private` in the main level

Create three files in this folder.

`config.ini`, `RSA key`

the config.ini file is where blog.py looks for the configurations

    :::code
    [server]
    user = xxx
    path = xxx-west-2.compute.amazonaws.com
    folder = /var/xxx

    [other]
    key = private/RSA Key



## Set up 
The blog.py lets you do 3 things

`python blog.py` runs the website in your local address.   

`python blog.py build` builds the static website using Python Flask's `freeze`. The website is stored in the `build` folder.

`python blog.py deploy` deploys the website based on the configurations.


