# Import Flask class from flask library. (Note the upper/lowercase conventio
from flask import Flask, render_template

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-­website.com/").
# Could be instead "my­website.com/about" or anything ­ more on this later.
@app.route('/')
# Function that returns the page: Display "Hello, World!"
def index():
   return '<ol><li>Chocolate</li>      <li>Strawberry</li>     <li>Vanilla</li></ol>'
   return '<h1>Hello, World!</h1 >'

@app.route('/myself')
def self_intro():
   return 'My name is Deadpool!'

# @app.route('/html_reading')
# def read_html():
#    return render_template('html_demo.html')

@app.route('/myPage')
def read_html():
   return render_template('meor_page.html')


if __name__ == '__main__':
   app.run(debug=True)