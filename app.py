from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Sample Jenkins Multi-Stage Pipeline Integrated and few changes yet to be added"


if __name__ == "__main__":
    app.run(debug=True)
