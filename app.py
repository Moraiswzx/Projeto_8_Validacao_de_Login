from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('login.html')

@app.route('/cadastrar', methods=['POST', 'GET'] )
def cadastrar():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']

        return f'CADASTRO CONCLUÍDO! Seja bem vindo {nome}! {email} - {senha}'
    
    return render_template('cadastrar.html')

if __name__ == "__main__":
    app.run(debug=True)