from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,world! welcome to python heroku world"

if __name__ == "__main__":
    app.run()



