#Autor - Felipe Siedschlag Yopán
#Feito como parte do desafio do sistema de seleção de estágio da Certi

unidades = ('zero','um','dois','tres','quatro',
	'cinco', 'seis', 'sete', 'oito', 'nove')

xi_xix = ('onze', 'doze', 'treze', 'quatorze', 'quinze',
	'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez','vinte','trinta','quarenta','cinquenta',
	'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('', 'cento','duzentos','trezentos','quatrocentos','quinhentos',
	'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

def numero_com_2_digitos(valor):
	if valor == '10':
		texto = dezenas[1]
	elif valor == '20':
		texto = dezenas[2]
	elif valor[1] == '0':
		texto = dezenas[int(valor[0])]
	else:
		texto = dezenas[int(valor[0])] + ' e ' + unidades[int(valor[1])]
	return texto

def numero_com_3_digitos(valor):
	if valor == '100':
		texto = 'cem'
	elif valor[1] == '0' and valor[2] == '0':
		texto = centenas[int(valor[0])]
	elif valor[1] == '0':
		texto = centenas[int(valor[0])] + ' e ' + unidades[int(valor[2])]
	elif valor[2] == '0':
		texto = centenas[int(valor[0])] + ' e ' + dezenas[int(valor[1])]
	else:
		texto = centenas[int(valor[0])] + ' e ' + dezenas[int(valor[1])] + ' e ' + unidades[int(valor[2])]
	return texto

def numero_com_4_digitos(valor):
	if valor == '1000':
		texto = 'mil'
	elif valor[0] == '1':
		texto = 'mil e ' + numero_com_3_digitos(valor[1:])
	return texto

def tradutor(entrada):
	negativo = entrada.startswith('-')

	#Pegar apenas o valor absoluto, com tipo string mesmo
	if  negativo == True:
		#Copia entrada elimiando o primeiro caractere
		valor = entrada[1:]
	else:
		valor = entrada

	#Verica o tamanho em dígitos do valor
	tamanho = len(valor)

	if tamanho == 1:
		saida = unidades[int(valor)]

	elif tamanho == 2:
		saida = numero_com_2_digitos(valor)

	elif tamanho == 3:
		saida = numero_com_3_digitos(valor)

	elif tamanho == 4:
		saida = numero_com_4_digitos(valor)

	#Adicionar sinal negativo?
	if negativo == 1:
		saida = 'menos ' + saida

	return saida

while True:
	entrada = input('Informe um numero de 0 a 999: ')
	print(tradutor(entrada))