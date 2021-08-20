from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/crear_empresa')
def crear_empresa():
    return render_template('crear_empresa.html')

@app.route('/crear_operadora')
def crear_operadora():
    return render_template('crear_operadora.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)