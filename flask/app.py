from flask import Flask,render_template
# It creates an instance of the flask class,
# which is the WSGI application.

# wsgi application is a web application that is executed by the web server.
app=Flask(__name__)
@app.route('/')
def welcome():
    return "<h1 >Welcome to the Homeeeesssee Page<h1>"
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

# the below line will run first in the entire code.
if __name__ == '__main__':
    app.run(debug=True)