# First we imported the Flask class. 
# An instance of this class will be our WSGI application.
from flask import Flask


# Next we create an instance of this class. 
# The first argument is the name of the application’s module or package. 
# __name__ is a convenient shortcut for this that is appropriate for most cases.
# This is needed so that Flask knows where to look for resources such as
# templates and static files.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello word"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

