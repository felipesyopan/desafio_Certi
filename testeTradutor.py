import logica

arquivo = open('provaReal.txt', 'w')

for i in range(-99999,100000):
	letra = str(i)
	linha = letra + ' -> ' + logica.tradutor(letra) + '\n'
	arquivo.write(linha)

arquivo.close()