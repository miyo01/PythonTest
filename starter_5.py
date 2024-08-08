from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Variables to pass to the template
    context = {
        'title': 'Welcome Page',
        'name': 'John Doe',
        'items': ['Apple', 'Banana', 'Cherry']
    }
    return render_template('index4.html', **context)

if __name__ == '__main__':
    app.run(debug=True)