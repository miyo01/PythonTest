from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return '<h1>Hello World! My name is Deeban</h1>\n<p> This is a paragraph</p>' 
    
@app.route('/mylist')

def listing():
    line1 = "<h1><b>Hello</b> World!</h1>"
    line2 = "<p>If music be the food of love, play on!</p>"
    line3 = "<img src='https://media.giphy.com/media/sWrDT2OqxJ3Fu/giphy.gif'>"
    total = line1 + line2 + line3
    return total
@app.route('/readinghtml')

def read_html():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)