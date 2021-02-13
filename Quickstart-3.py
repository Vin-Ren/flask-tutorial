# src: https://flask.palletsprojects.com/en/1.1.x/quickstart
# This part Contains The Following:
#1 File Uploads
#2 Cookies
#3 Redirects and Errors


# --Basic Flask Setup--
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
# --End Of Setup--


# File Uploads
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#file-uploads
# You can handle uploaded files with Flask easily. Just make sure not to forget
# to set the enctype="multipart/form-data" attribute on your HTML form, otherwise
# the browser will not transmit your files at all.

# how to set the enctype: https://www.w3schools.com/tags/att_form_enctype.asp

# Uploaded files are stored in memory or at a temporary location on the filesystem.
# You can access those files by looking at the files attribute on request object.
# Each uploaded file is stored in that dictionary.

# It behaves just like a standard Python file object, but it also has a save()
# method that allows you to store that file on the filesystem of the server.
# Here's a simple example showing how that works:
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/data/uploads/uploaded_file.txt')
        return 'Saved'

# If you want to know how the file was named on the client before it was
# uploaded to you app, you can access the filename attribute. However please
# keep in mind that this value can be forged so never ever trust this value.

# If you want to use the filename of the client to store the file on the server,
# pass it through the secure_filename() function that Werkzeug provides for you
# Example:
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload2', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f'/data/uploads/{secure_filename(f.filename)}')
        return 'Saved'

# For some better examples, checkout the Uploading Files pattern.
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files



# --References--
# save(): https://werkzeug.palletsprojects.com/en/1.0.x/datastructures/#werkzeug.datastructures.FileStorage.save
# f.filename: https://werkzeug.palletsprojects.com/en/1.0.x/datastructures/#werkzeug.datastructures.FileStorage.filename
# secure_filename(): https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.utils.secure_filename
# Better Examples: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files





# Cookies
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies

# To access cookies you can use the cookies attribute. To set cookies you can
# use the set_cookie() method of response objects. The cookies attribute
# of request objects is a dictionary with all the cookies the client transmits.

# If you want to use sessions, do not use the cookies directly, Instead use
# the Sessions in Flask that add some security on top of cookies for you
# Sessions: https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions

# Better example: https://pythonbasics.org/flask-cookies/
# Examples
# Reading cookies:
from flask import request

@app.route('/read_cookies')
def read_cookies():

    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return render_template('cookies.html', username=user)

# Storing cookies:
from flask import make_response

@app.route('/set_cookies')
def set_cookies():
    resp = make_response(render_template('cookies.html'))
    resp.set_cookie('username', 'John Doe')
    return resp

# Combined:
from flask import request, make_response

@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    username = request.cookies.get('username')
    if username is not None:
        return render_template('cookies.html', username=username)
    else:
        resp = make_response(render_template('cookies.html'))
        resp.set_cookie('username', 'John Doe')
        return resp

# The combined example on first run would say:
# Hello, seems like you're setting your cookies?
# Then the second run and so on would say:
# Your cookies says you're John Doe.

# If you want to try it, feel free to clear your cookies through:
# Inspect> Network> Name> Cookies> Rightclick> Clear browser cookies.


# Note: The examples of cookies has slightly tampered.
# Visit the documentation for the real example.
# I changed the examples so that there's no conflict and for better explanation.

# Note that cookies are set on response objects. Since you normally just return
# strings from the view functions Flask will convert them into response object
# for you. If you explicitly want to do that you can use the make_response()
# funciton and then modify it.

# Sometimes you might want to set a cookie at a point where the response object
# does not exist yet. This is possible by utilizing
# the Deferred Request Callbacks pattern.

# For this also see About Responses.



# --References List--
# Cookies: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.cookies
# Sessions: https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
# make_response(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
# Deferred Request Callbacks: https://flask.palletsprojects.com/en/1.1.x/patterns/deferredcallbacks/#deferred-callbacks
# Responses: https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses





# Redirects and Errors
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors
# To redirect a user to another endpoint, use the redirect() function.
# To abourt a request early with an error code, use the abort() function.

# Example:
from flask import abort, redirect, url_for

@app.route('/redirect')
def redirect():
    return redirect(url_for('login4'))

@app.route('/login4')
def login4():
    abort(401) # abort(error code)
    this_is_never_executed() # some code to never be executed.

# This is a rather pointless example because a user will be redirected from
# the redirect page to a page they cannot access (401 means access denied)
# but it shows how it works.

# By default a black and white error page is shown for each error code. If you
# want to customize the error page, you can use the errorhandler() decorator:

from flask import render_template

@app.errorhandler(404) # Pass in the error code to be handled
def page_not_found(error):
    return render_template('404_error_page.html', error=error), 404

# Note the 404 after render_template() call. This tells Flask that the status
# code of that page should be 404 which means not found. By default 200 is
# assumed which translates to: all went well.

# See Error handlers for more details.



# --References--
# Redirect(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect
# abort(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.abort
# errorhandler(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.errorhandler
# render_template(): https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template
# Error handlers: https://flask.palletsprojects.com/en/1.1.x/errorhandling/#error-handlers
