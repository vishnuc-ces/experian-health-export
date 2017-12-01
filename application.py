from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def corporation():
    return render_template('corporation.html')

@app.route('/branch')
def branch():
    return render_template('branch.html')

if __name__ == '__main__':
    app.run()