from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Vercel requires this, but doesn't use the 'run' command
if __name__ == '__main__':
    app.run()