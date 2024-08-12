### Q1. What is Flask Framework? What are the advantages of Flask Framework?
#Flask is a lightweight web framework for Python, offering flexibility with minimal setup. Its advantages include simplicity, scalability, and support for extensions.

### Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.
#Here’s a simple Flask application:

from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'
@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/get-url')
def get_url():
    return url_for('about')

@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation"

@app.route('/')
def details():
    return '''
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999
    '''

if __name__ == '__main__':
    app.run()


#(Please run this code in your environment and share the screenshot.)

### Q3. What is App routing in Flask? Why do we use app routes?
#App routing in Flask maps URLs to specific functions. We use app routes to define different URLs and connect them with corresponding view functions.

### Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” route to show the following details:


#(Please run this code in your environment and share the screenshot.)

### Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
#The `url_for()` function in Flask is used for URL building, allowing you to dynamically generate URLs for your view functions. Here's an example:


