# src: https://flask.palletsprojects.com/en/1.1.x/quickstart
# This Part Contains The Following:
#1 Basic Setup
#2 Routing
#3 Running The Web Application
#4 Debug Mode
#5 Variable Rules
#6 Unique URLs and or Redirection Behavior

# Basic Setup or Minimal App
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
from flask import Flask

# Creating an instance of Flask
# __name__ variable is needed, because depending if it's started as application
# or imported as module the name would be different. so __name__ is needed so
# that flask knows where to look for templates static files, and so on.
app = Flask(__name__)


# Routing
# Route decorator to tell flask what url should trigger the function.
# A single function can have multiple route decorator.
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
# If accessed through localhost, you should enter the url like:
# 127.0.0.1:5000/hello and not 127.0.0.1/hello:5000
# The second one would not work and just throw 'ERR_CONNECTION_REFUSED'
@app.route('/')
def index():
    return 'The Index Page.'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# --References--
# route(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route



# Running The Web App
# '>' is only a prefix.

# Run Through Terminal.
# >set FLASK_APP=<file name>.py
# >py -m flask run or >python -m flask run
# On Linux, <set> is changed to <export>





# Debug Mode
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode
# >set FLASK_ENV=development
# >flask run
# On Linux, <set> is changed to <export>
# Debug Mode Does The Following:
# it activates the debugger
# it activates the automatic reloader
# it enables the debug mode on the Flask application.





# Variable Rules
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
# NOTE: Recommended to be read on the documentation.

from markupsafe import escape
# escape function escapes text and returns a Markup object.
# the object won't be escaped anymore, but the text that is used with it will be,
# ensuring that the result remains safe to use in HTML.
# src: https://markupsafe.palletsprojects.com/en/1.1.x/

# You can add variable sections to a URL by making sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
# Optionally you can use a converter to specify the type of argument like
# <converter:variable_name>
# Examples:

@app.route('/user/<username>')
def show_user_profile(username):
    # Shows the user profile for the user
    # maybe do something like database[username]
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Shows the post with the given id, id is an integer
    return f'Post {str(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

# Converter types:
# String | (Default) Accepts any text without a slash.
# Int | Accepts positive integers.
# Float | Accepts positive floating point values
# Path | Like String but also accepts slashes
# Uuid | accepts UUID strings





# Unique URLs and or Redirection Behavior
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#unique-urls-redirection-behavior


@app.route('/projects/')
def projects():
    return 'The Project Page.'
#
# The canonical URL for the projects endpoint has a trailing slash.
# It's similiar to a folder in a file system. If you access the URL without
# a trailing slash, Flask redirects you to the canonical URL with the trailing slash.


@app.route('/about')
def about():
    return 'The About Page.'
#
# The canonical URL for the about endpoint does not have a trailing slash.
# It's similiar to the pathname of a file. Accesing the URL without a trailing
# slash produces a 404 'Not Found' error. This helps keep URLs unique for these
# resources, which helps search engines avoid indexing the same page twice.

# Canonical synonyms: legal, orthodox, approved, received, official.
