from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # We render the cringe html file
    return render_template('index.html')

if __name__ == '__main__':
    # Debug mode is on so you can see errors if you miss a file
    app.run(debug=True, port=5000)