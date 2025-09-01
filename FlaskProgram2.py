from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Balachander</h1>'


@app.route('/index')
def bala():
    return render_template('index.html')

@app.route('/index1/<name>')
def ba(name):
    return f'Welcome {name}'


if __name__=='__main__':
    app.run(debug=True)
