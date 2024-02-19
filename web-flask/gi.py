from flask import Flask

#note to self: to run app, switch to app dir, type "python -m flask --app <appName> run"

app = Flask("__name__")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if '__name__' == '__main':
    app.run(debug=True)