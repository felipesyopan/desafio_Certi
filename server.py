from flask import Flask
import json
import logica

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
	return "Digite um valor entre -99999 a 99999 na url! Por exemplo: localhost:3000/42"

#Recebe o que vier na URL como a string 'entrada'
@app.route("/<string:entrada>", methods = ["GET"])
def traduzir(entrada):

	#Condições de checkagem para as entradas válidas:
	#	- String com número decimal positivo com menos de 6 dígitos
	#	ou
	#	- String começando com o caractere '-', 
	#	onde o restante dos caracteres formam um decimal e o tamanho total é menor que 7. 
	if ( entrada.isdecimal() and len(entrada) < 6 ) or ( entrada.startswith('-') and entrada[1:].isdecimal() and len(entrada) < 7):
		#Cria a resposta contendo o numeral por extenso usando a função tradutor
		resposta = logica.tradutor(entrada)
		#Cria um dicionário python com a chave 'extenso' e o valor 'resposta'
		dicionario = { "extenso": resposta }
		#Converte o dicionário para JSON
		resultado_json = json.dumps(dicionario)
		#Envia o JSON como resultado da requisição.
		return resultado_json
	else:
		#Aviso para caso o usuário digite algo irregular.
		return "Entrada irregular!"

if __name__ == "__main__":
	#A porta padrão do flask é a 5000, aqui apenas mudo para 3000, conforme requerido.
	app.run(port=3000)