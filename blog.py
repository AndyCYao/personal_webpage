import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from configparser import ConfigParser
from subprocess import call 

DEBUG = True 
FLATPAGES_AUTO_RELOAD = DEBUG 
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)
freezer = Freezer(app)
config = ConfigParser()
config.read('private/config.ini')

@app.route("/")
def index():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    # return "hello, world!"
    return render_template('index.html', posts=posts)
    

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    # return post.html
    return render_template('page.html', page=post)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "deploy":
        print("Deploying..")
        freezer.freeze()
        key =       config.get('other', 'key')
        user =      config.get('server', 'user')
        path =      config.get('server', 'path')
        folder =    config.get('server', 'folder')
        deployCall = "scp -i {} -r build {}@{}:{}".format(key, user, path, folder)
        print(deployCall)
        call(deployCall)

    else:
        app.run(debug=True)

