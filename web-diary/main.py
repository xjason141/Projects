from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/owner')
def user():
    rqst = request.args
    owner = rqst.get('name')
    return render_template('user.html', name=owner)

#return json
@app.route('/json')
def get_json():
    return jsonify({'dict data in here'})

#get json data/accept json request
@app.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

#redirect to home
@app.route('/go-to-home')
def go_home():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)