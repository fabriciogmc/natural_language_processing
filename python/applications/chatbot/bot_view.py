from flask import Flask, render_template

app = Flask(__name__)
# Basic front-end route
@app.route('/')
def bot_service():
    return render_template("view.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)