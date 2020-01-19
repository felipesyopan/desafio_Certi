import logica

arquivo = open('provaReal.txt', 'w')

for i in range(-999,1200):
	letra = str(i)
	linha = letra + ' -> ' + logica.tradutor(letra) + '\n'
	arquivo.write(linha)

arquivo.close()