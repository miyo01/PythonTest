from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Call the external API
    response = requests.get("https://api.example.com/data")
    data = response.json()  # Convert the response to JSON format

    # Pass the data to the HTML template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)