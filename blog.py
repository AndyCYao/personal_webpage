import sys
from flask import Flask, render_template, send_file
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from configparser import ConfigParser
from fabric.api import local
# from pygments import pygments_style_defs
from unicodedata import normalize
from datetime import date, datetime
import codecs
import re
import os

DEBUG = True 
BASE_URL = 'https://andy-yao.com'
FLATPAGES_AUTO_RELOAD = DEBUG 
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
# FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code']
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

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs(style='colorful'), 200, {'Content-Type': 'text/css'}

############
# Blog Helper
def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def createPost():
    print("Create new post..")
    section  = raw_input("What is the section? Options- [posts, courses]\n")
    title    = raw_input("What is the title? *Optional\n")
    summary  = raw_input("What is the summary? *Optional\n")
    filename = raw_input("What is the file name? *Optional\n")
    post(section, title, summary, filename)

def post(section, title=None, summary=None, filename=None):
    """ Create a new empty post.
    """
    if not os.path.exists(os.path.join(FLATPAGES_ROOT, section)):
        raise u"Section '%s' does not exist" % section
    post_date = datetime.today()
    title = unicode(title) if title else "Untitled Post"
    if not filename:
        filename = u"%s.md" % slugify(title)
    year = post_date.year
    # pathargs = [section, str(year), filename, ]
    pathargs = [section, filename, ]
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        FLATPAGES_ROOT, '/'.join(pathargs))
    if os.path.exists(filepath):
        raise "File %s exists" % filepath
    content = '\n'.join([
        u"title: %s" % title,
        u"date: %s" % post_date.strftime("%Y-%m-%d"),
        u"summary: %s" % summary,
        u"image: ",
        u"published: false\n\n",
    ])
    try:
        codecs.open(filepath, 'w', encoding='utf8').write(content)
        print(u'Created %s' % filepath)
    except Exception, error:
        raise error

############

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
    elif len(sys.argv) > 1 and sys.argv[1] == "new":
        createPost()
    else:
        app.run(host="0.0.0.0", debug=True)

