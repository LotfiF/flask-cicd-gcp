import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("Name", "World ! V2")
    return f"Hello {name}"

def sum(a, b):
    return a + b

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))) 
    
# import os    
# from flask import Flask, request
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello'

# @app.route('/calc')
# def calc():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     return str(sum(int(a), int(b)))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
