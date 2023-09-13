from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    data = request.args
    return data
    # return "<p>Hello, World tesss!</p>"

if __name__ == '__main__':
    app.run('0.0.0.0', 5050, debug=True)