from flask import Flask



app = Flask(__name__)



# mysql = MySQL(app)





@app.route('/')
def hello():
    return 'Hello, Flask app with a virtual environment!'

if __name__ == '__main__':
    app.run(debug=True)
