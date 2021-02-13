# src: https://flask.palletsprojects.com/en/1.1.x/quickstart
# This part Contains The Following:
#1 URL building
#2 HTTP Methods
#3 Static Files
#4 Rendering Templates
#5 The Request Object

# URL Building
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building
# To build a URL to a specific function, use the url_for() function.
# It accepts the name of the function as its first argument and any number of
# keyword arguments, each corresponding to a variable part of the URL rule.
# Unknown variable parts are appended to the URL as query parameters.
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

# Ultilizing Variable Rules From Part 1
@app.route('/user/<username>')
def profile(username):
    return f"{username}'s Profile"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
# Example Use Case:
# https://stackoverflow.com/a/35936261/15110097



# --References--
# url_for(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.url_for
# test_request_context(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_request_context
# Context Locals: https://flask.palletsprojects.com/en/1.1.x/quickstart/#context-locals





# HTTP Methods
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
# Web app use different HTTP methods when accessing URLs. You soud familiarize
# Yourself with the HTTP methods as you work with Flask. By default, a route
# only answers to 'GET' requests. You can use the 'methods' argument of the 'route()'
# decorator to handle different HTTP methods.
from flask import request

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()

# Note: GET method is the default method of browsers when you visits a webpage.



# --References--
# route(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route
# HTTP RFC: https://www.ietf.org/rfc/rfc2068.txt





# Static Files
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
# Dynamic web app still need static files. That's usually where the CSS and Javascript
# files are coming from. Ideally your web server is configured to server them
# for you, but during development Flask can do that as well. Just create a folder
# called 'static' in your package or next to your module and it will be available
# at '/static' on the application.

# to generate URLs for static files, use the special 'static' endpoint name.
# Example:
# foo = url_for('static', filename='style.css')

# The file has to be stored on the filesystem as 'static/style.css'





# Rendering Templates
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
# Flask configures the Jinja2 template engine for you automatically.

# To render a template you can use the render_tempalate() method.
# All you have to do is provide the name of the template and the variables you
# want to pass to the template engine as keyword arguments.
# Here's a simple Example:
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Flask will look for template in the templates folder.
# The path tree should look like this:
#/application.py
#/templates
#    /hello.html

# As for the templates, you can use the full powe rof jinja2 templates.
# Head over to the official Jinja2 documentation for more information:
# http://jinja.pocoo.org/docs/templates/

# An example template has already been created for you, at ./template/hello.html


# Inside the templates you also have access to the request, session and g objects
# as well as the get_flashed_messages() function.
# request: https://flask.palletsprojects.com/en/1.1.x/api/#flask.request
# session: https://flask.palletsprojects.com/en/1.1.x/api/#flask.session
# g object is something in which you can store information for your own needs.
# g object: https://flask.palletsprojects.com/en/1.1.x/api/#flask.g

# Templates are especially useful if inheritance is used. Head over to the docs
# to learn how it works.
# https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/#template-inheritance

# Auto escaping is enabled, so if 'name' contains HTML it will be escaped automatically.
# If you can trust a variable and you know that it will be safe HTML,
# you can mark it safe by using the Markup class or by using the |safe filter
# in the template.
# as always, head to Jinja2 Documentation for more examples:



# --References--
# Jinja2: http://jinja.pocoo.org/
# render_template(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template
# Jinja2 Templates: http://jinja.pocoo.org/docs/templates/
# request: https://flask.palletsprojects.com/en/1.1.x/api/#flask.request
# session: https://flask.palletsprojects.com/en/1.1.x/api/#flask.session
# g object: https://flask.palletsprojects.com/en/1.1.x/api/#flask.g
# get_flashed_messages(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.get_flashed_messages
# Template Inheritance: https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/#template-inheritance
# Markup: https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Markup





# The Request Object
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
# This Part Isn't going into the details of the request object, instead it would
# go through some of the most common operations.
# first you'll have to import it from the flask module
from flask import request

# The current request mothod is available by using the method attribute.
# To access form data(data transmitted in a POST or PUT request) you can use
# the form atrribute. Here is a full example of the two attributes mentioned above.

# Changed login to login3 to avoid conflicts with other sections
@app.route('/login3', methods=['POST', 'GET'])
def login3():
    error=None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # The code below is executed if the request method was GET
    # or the credentials were invalid.
    return render_template('hello.html', name=error)
    # just using the hello.html template for demonstration purposes.

# If the key does not exist in the form attribute, a special KeyError is raised.
# You can catch it like a standard KeyError but if you don't,
# a HTTP 400 Bad Request error page is shown instead. So for many situations you
# don't have to deal with that problem.


# To access parameters submitted in the URL (?key=value) you can use
# the args attribute:
# request.args behave simiarly to a dictionary.
# because it's similiar to a dictionary, you can use get(key, default) or [key]

#value = request.args.get('key', '')

# Flask documentation recommends accessing URL parameters with get() method
# or by catching KeyError because users might change the URL and presenting
# them a 400 Bad Request error page in that case is not user friendly.
# For a full list of methods and attributes of the request object:
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request



# --References--
# request: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request
# request.method: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.method
# request.form: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.form
# request.args: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.args
