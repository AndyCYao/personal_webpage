import sys
from flask import Flask, render_template, send_file
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from configparser import ConfigParser
from fabric.api import local
# from pygments import pygments_style_defs
# import pygments

DEBUG = True 
BASE_URL = 'https://andy-yao.com'
FLATPAGES_AUTO_RELOAD = DEBUG 
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'

POST_DIR = 'posts'
COURSES_DIR = 'courses'

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

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('page.html', page=post)

@app.route('/courses/')
def courses():
    courses = [c for c in flatpages if c.path.startswith(COURSES_DIR)]
    # print(courses)
    return render_template('courses.html', courses = courses)

@app.route('/courses/<name>/')
def course(name):
    path = '{}/{}'.format(COURSES_DIR, name)
    course = flatpages.get_or_404(path)
    return render_template('page.html', page = course)

@app.route("/cv.pdf")
def cv():
    return send_file('static/assets/cv.pdf')

'''
@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
'''

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        # local("cp -r static/assets build")
    elif len(sys.argv) > 1 and sys.argv[1] == "deploy":
        print("Deploying..")
        freezer.freeze()
        key =       config.get('other', 'key')
        user =      config.get('server', 'user')
        path =      config.get('server', 'path')
        folder =    config.get('server', 'folder')
        deployCall = "scp -i {} -r build {}@{}:{}".format(key, user, path, folder)
        local(deployCall)

    else:
        app.run(debug=True)

