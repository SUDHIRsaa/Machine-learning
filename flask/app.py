from flask import Flask,render_template,request
# It creates an instance of the flask class,
# which is the WSGI application.

# wsgi application is a web application that is executed by the web server.
app=Flask(__name__)
@app.route('/')
def welcome():
    return "<h1 >Welcome to the Homeeeesssee Page<h1>"
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        return f"<h1> Name:<i> {name} <i/> Email: <i>{email}<i/>  <i>Password: {password}<h1/>" 
        
    return render_template('form.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        return f"<h1> Name:<i> {name} <i/> Email: <i>{email}<i/>  <i>Password: {password}<h1/>" 
        
    return render_template('form.html')


# the below line will run first in the entire code.
if __name__ == '__main__':
    app.run(debug=True)