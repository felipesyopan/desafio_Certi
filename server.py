from flask import Flask
import json
import logica

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
	return "Digite um valor entre -99999 a 99999 na url! Por exemplo: localhost:3000/42"

@app.route("/<string:entrada>", methods = ["GET"])
def traduzir(entrada):
	#Se a string de entrada representa um valor decimal,
	#ou começa com '-' e o restante dela representa um valor decimal, traduz e responde.
	#Caso contrário, o formato é irregular e envia um aviso como resposta!
	if entrada.isdecimal() or ( entrada.startswith('-') and entrada[1:].isdecimal() ):
		resposta = logica.tradutor(entrada)
		dicionario = { "extenso": resposta }
		resultado_json = json.dumps(dicionario)
		return resultado_json
	else:
		return "Entrada irregular!"

if __name__ == "__main__":
	app.run(port=3000)