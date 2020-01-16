unidades = ('zero','um','dois','tres','quatro',
	'cinco', 'seis', 'sete', 'oito', 'nove')

xi_xix = ('onze', 'doze', 'treze', 'quatorze', 'quinze',
	'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez','vinte','trinta','quarenta','cinquenta',
	'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('', 'cento','duzentos','trezentos','quatrocentos','quinhentos',
	'seiscentos', 'setecentos', 'oitocentos', 'novecentos')


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
		if valor == '10':
			saida = dezenas[1]
		elif valor == '20':
			saida = dezenas[2]
		elif valor[1] == '0':
			saida = dezenas[int(valor[0])]
		else:
			saida = dezenas[int(valor[0])] + ' e ' + unidades[int(valor[1])]

	elif tamanho == 3:
		if valor == '100':
			saida = 'cem'
		elif valor[1] == '0' and valor[2] == '0':
			saida = centenas[int(valor[0])]
		elif valor[1] == '0':
			saida = centenas[int(valor[0])] + ' e ' + unidades[int(valor[2])]

		elif valor[2] == '0':
			saida = centenas[int(valor[0])] + ' e ' + dezenas[int(valor[1])]
		else:
			saida = centenas[int(valor[0])] + ' e ' + dezenas[int(valor[1])] + ' e ' + unidades[int(valor[2])]

	elif tamanho == 4:
		if valor == '1000':
			saida = 'mil'
		elif valor[1] == '0' and valor[2] == '0' and valor[3] == '0':
			saida = unidades[int(valor[0])] + ' mil'
		elif valor[1] == '0' and valor[2] == '0':
			saida = unidades[int(valor[0])] + ' mil e ' + unidades[int(valor[3])]
		elif valor[1] == '0':
			saida = unidades[int(valor[0])] + ' mil e ' + dezenas[int(valor[2])] + ' e ' + unidades[int(valor[3])]
		else:
			saida = unidades[int(valor[0])] + ' mil e ' + centenas[int(valor[1])] + ' e ' + dezenas[int(valor[2])] + ' e ' + unidades[int(valor[3])]


	#Adicionar sinal negativo?
	if negativo == 1:
		saida = 'menos ' + saida

	return saida

while True:
	entrada = input('Informe um numero de 0 a 999: ')
	print(tradutor(entrada))