unidades = ('zero','um','dois','tres','quatro',
	'cinco', 'seis', 'sete', 'oito', 'nove')

xi_xix = ('onze', 'doze', 'treze', 'quatorze', 'quinze',
	'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez','vinte','trinta','quarenta','cinquenta',
	'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('', 'cento','duzentos','trezentos','quatrocentos','quinhentos',
	'seiscentos', 'setecentos', 'oitocentos', 'novecentos')


def tradutor(entrada):
	tamanho = len(entrada)
	neg = entrada.find('-')
	if neg == -1:
		#print('Não é negativo')
		negativo = 0
	else:
		tamanho = tamanho-1
		negativo = 1

	if tamanho == 1:
		saida = unidades[int(entrada)]

	elif tamanho == 2:
		if entrada == '10':
			saida = dezenas[1]
		elif entrada == '20':
			saida = dezenas[2]
		elif entrada[1] == '0':
			saida = dezenas[int(entrada[0])]
		else:
			saida = dezenas[int(entrada[0])] + ' e ' + unidades[int(entrada[1])]

	elif tamanho == 3:
		if entrada == '100':
			saida = 'cem'
		elif entrada[1] == '0':
			saida = centenas[int(entrada[0])] + ' e ' + unidades[int(entrada[2])]

		elif entrada[2] == '0':
			saida = centenas[int(entrada[0])] + ' e ' + dezenas[int(entrada[1])]
		else:
			saida = centenas[int(entrada[0])] + ' e ' + dezenas[int(entrada[1])] + ' e ' + unidades[int(entrada[2])]

	#Adicionar sinal negativo?
	if negativo == 1:
		saida = 'menos' + saida

	return saida

while True:
	entrada = input('Informe um numero de 0 a 999: ')
	print(tradutor(entrada))