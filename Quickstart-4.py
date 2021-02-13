# src: https://flask.palletsprojects.com/en/1.1.x/quickstart
# This part Contains The Following:
#1 About Responses

# --Basic Flask Setup--
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
# --End Of Setup--





# About Responses
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses
# NOTE: It is recommended that this section is read on the documentation.

# Return value of a view function is automatically converted into a response
# object for you. If the return value is a string then it's converted into
# a response object with the string as response body, a 200 OK status code
# and a text/html mimetype.

# If the return value is a dict, jsonify() is called to produce a response.
# The logic is that Flask applies to converting return vlaues into response
# objects is as follows:

#1 If a response object of the correct type is returned, it's directly returned from the view.
#2 If it's a string, a response object is created with that data and default parameters.
#3 If it's a dict, a response object is created using jsonify().
#4 If a tuple is returned, the items in the tuple can provide extra information.
#  such tuples have to be in the form (response, status), (response, headers),
#  or (response, status, headers). The status value will override the status code
#  and headers can be a list or dictionary of additional header values.
#5 If none of that works, Flask will assume the return value is a valid WSGI
#  application and convert that into a response object.


# If you want to get hold of the resulting response object inside the view
# you can use the make_response() function.

# for example, imagine you have a view like this:
'''
@app.errorhandler(404)
def not_found(error):
    return render_template(error.html), 404
'''
# You just need to wrap the return expression with make_response() and get the
# response object to modify it, then return it.
from flask import make_response, render_template
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404_error_page.html'), 404)
    resp.headers['X-Something'] = 'A Value'
    return resp

# The header value can be seen through:
# Inspect > Network > All > Name > Some subpath > Headers > Response Headers
