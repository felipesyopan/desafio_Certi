from flask import Flask
import json
import logica

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
	return "Digite um valor entre -99999 a 99999 na url! Por exemplo: localhost:3000/42"

@app.route("/<string:entrada>", methods = ["GET"])
def traduzir(entrada):

	if ( entrada.isdecimal() and len(entrada) < 6 ) or ( entrada.startswith('-') and entrada[1:].isdecimal() and len(entrada) < 7):
		resposta = logica.tradutor(entrada)
		dicionario = { "extenso": resposta }
		resultado_json = json.dumps(dicionario)
		return resultado_json
	else:
		return "Entrada irregular!"

if __name__ == "__main__":
	app.run(port=3000)