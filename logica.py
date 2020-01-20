#Autor - Felipe Siedschlag Yopán
#Feito como parte do desafio do sistema de seleção de estágio da Certi

#Tuplas guardando as strings usadas para formar os números por extenso:
################################################################################
unidades = ('zero','um','dois','tres','quatro',
	'cinco', 'seis', 'sete', 'oito', 'nove')

xi_xix = ('onze', 'doze', 'treze', 'quatorze', 'quinze',
	'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez','vinte','trinta','quarenta','cinquenta',
	'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('', 'cento','duzentos','trezentos','quatrocentos','quinhentos',
	'seiscentos', 'setecentos', 'oitocentos', 'novecentos')
################################################################################

#Função responsável por tratar números com 2 dígitros
def numero_com_2_digitos(valor):
	valor_int = int(valor)

	#Filtragem dos números 11-19
	if valor_int > 10 and valor_int < 20:
		texto = xi_xix[valor_int-11]

	#Regras para os outros valores
	else:
		#Caso em que haja zero à esquerda
		if valor[0] == '0':
			texto = unidades[int(valor[1])]
		#Caso em que haja o zero à direita, para não haver, por exemplo, 'vinte e zero'.
		elif valor[1] == '0':
			texto = dezenas[int(valor[0])]
		#Caso geral
		else:
			texto = dezenas[int(valor[0])] + ' e ' + unidades[int(valor[1])]

	return texto

#Função responsável por tratar números com 3 dígitros
def numero_com_3_digitos(valor):
	#Caso único em que ocorre 'cem', o restante usa 'cento'
	if valor == '100':
		texto = 'cem'
	#Caso o número venha no formato '00X'
	elif valor[0] == '0' and valor[1] == '0':
		texto = unidades[int(valor[2])]
	#Caso o número venha no formato 'X00'
	elif valor[1] == '0' and valor[2] == '0':
		texto = centenas[int(valor[0])]
	#Caso com um zero à esquerda
	elif valor[0] == '0':
		texto = numero_com_2_digitos(valor[1:])
	#Caso geral
	else:
		texto = centenas[int(valor[0])] + ' e ' + numero_com_2_digitos(valor[1:])
	return texto

#Função responsável por tratar números com 4 dígitros
def numero_com_4_digitos(valor):
	#Específico parar 1000, caso contrário daria um mil...
	if valor == '1000':
		texto = 'mil'
	#Caso em que o dígito de milhar é '1', também para não ficar 'um mil'
	elif valor[0] == '1':
		texto = 'mil e ' + numero_com_3_digitos(valor[1:])
	#Caso para as unidades de milhar, evita que a resposta seja 'dois mil e zero', por exemplo
	elif valor[1] == '0' and valor[2] == '0' and valor[2] == '0':
		texto = unidades[int(valor[0])] + ' mil'
	#Caso com zero à esquerda
	elif valor[0] == '0':
		texto = numero_com_3_digitos(valor[1:])
	else:
	#Caso geral
		texto = unidades[int(valor[0])] + ' mil e ' + numero_com_3_digitos(valor[1:])
	return texto

def numero_com_5_digitos(valor):
	#Aqui o número é separado em duas partes, uma correspondente aos milhares,
	#e outra às centenas.

	#Caso 00XXX
	if valor[0] == '0' and valor[1] == '0':
		texto = numero_com_3_digitos(valor[2:])
	#Caso XX000, evita que a resposta seja 'vinte e dois mil e zero', por exemplo
	elif valor[2] == '0' and valor[3] == '0' and valor[4] == '0':
		texto = numero_com_2_digitos(valor[:2]) + ' mil'
	#Caso geral
	else:
		texto = numero_com_2_digitos(valor[:2]) + ' mil e ' + numero_com_3_digitos(valor[2:])
	return texto

def tradutor(entrada):
	negativo = entrada.startswith('-')

	#Pegar apenas o valor absoluto, com tipo string mesmo
	if  negativo == True:
		#Copia entrada elimiando o primeiro caractere('-')
		valor = entrada[1:]
	else:
		#Copia a entrada na íntegra
		valor = entrada

	#Verifica o tamanho em dígitos do valor
	tamanho = len(valor)

	#O número é traduzido em função de seu tamanho em dígitos
	if tamanho == 1:
		saida = unidades[int(valor)]

	elif tamanho == 2:
		saida = numero_com_2_digitos(valor)

	elif tamanho == 3:
		saida = numero_com_3_digitos(valor)

	elif tamanho == 4:
		saida = numero_com_4_digitos(valor)

	elif tamanho == 5:
		saida = numero_com_5_digitos(valor)
	else:
		negativo = False
		#Resposta padrão caso use essa função em outro software
		saida = "Numero de tamanho invalido!"

	#Adicionar sinal negativo?
	if negativo == True:
		saida = 'menos ' + saida

	return saida

'''
...para os testes
while True:
	entrada = input('Informe um numero de -99999 a 99999: ')
	print(tradutor(entrada))
'''