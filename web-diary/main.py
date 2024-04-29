from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)