from flask import Flask

#note to self: to run app, switch to app dir, type "python -m flask --app <appName> run"

app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, Didi!'