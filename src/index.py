from flask import Flask, render_template, request, flash
from flask.helpers import url_for
# from redis import Redis
import requests
import json

from werkzeug.utils import redirect

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/crear_empresa')
def crear_empresa():
    return render_template('crear_empresa.html')

@app.route('/empresa_usuario')
def empresa_usuario():
    return render_template('empresa_usuario.html')

@app.route('/crear_operadora')
def crear_operadora():
    return render_template('crear_operadora.html')

@app.route('/realtime_usuarios')
def realtime_usuarios():
    return render_template('realtime_usuarios.html')

@app.route('/campañas')
def campañas():
    return render_template('campañas.html')

@app.route('/campañas_vista_empresa')
def campañas_vista_empresa():
    return render_template('campañas_vista_empresa.html')

@app.route('/mensajeria', methods=['GET','POST'])
def mensajeria():

    if request.method == 'POST':

        url = "http://20.62.155.25:8008/api/msg/send"

        payload = json.dumps({
        "from": request.form['from'],
        "to": request.form['to'],
        "text": request.form['text'],
        "dlr": False,
        "dlr_url": "string",
        "tag": "string",
        "profile": "string",
        "eta": "2021-09-23T20:10:04.309Z",
        "eta_seconds": 0,
        "retries": 0
        })
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(request.form)
        print(response.text)
        print(f"status:{response.status_code}")
        if response.status_code == 200:
            return render_template('mensajeria.html', msg = "Mensaje Enviado", flag = 'success')
        else:
            return render_template('mensajeria.html', msg = "No se ha podido envíar el mensaje", flag = 'danger')
    return render_template('mensajeria.html', msg = "")

@app.route('/configurar_operadora')
def configurar_operadora():
    return render_template('configurar_operadora.html')

@app.route('/test', methods=['POST'])
def test():
    
    return redirect(url_for('mensajeria'), msg = "Enviado")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)