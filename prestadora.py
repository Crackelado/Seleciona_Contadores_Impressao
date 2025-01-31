#! python3.10

# Importa as classes "run" e "PIPE" do módulo "subprocess", responsável para importar consultas feitas no terminal linux (shell) e passar para variável
from subprocess import run, PIPE

# Importa classe "datetime" do módulo "datetime", responsável para pegar datas e transformar em texto conforme necessário
from datetime import datetime

# Importa classe "argv" do módulo "sys". Pega os parâmetros passado para o arquivo .py antes da execução pelo terminal
from sys import argv

# Variável que armazena atalho da pasta onde ficam os prints de tela do computador
atalho = '/home/usuario/Downloads/'

# Variável que armazena atalho da pasta onde será criada para armazenar os prints enviados para prestadora. Sempre é gerado com a data: %ano(2 dígitos).%mês.%dia
atalho2 = '/home/usuario/Documents/Luiz2023/Prestadora/' + datetime.now().strftime('%y.%m.%d')

# Variável array para armazenar lista com o número de série das impressoras
imp = ['ZEQYBQAF4000CFW', 'ZEQYBQAF5001FLM', 'ZDDPB07K110ZF4Y', 'ZEQYBQAF6001RZL', 'ZDDPB07MA174KBW', '6TB443854']

# Variável array para pegar lista de prints
teste = []

# Tenta pegar o parâmetro passado antes de executar arquivo
try:

	# Os parâmetros são passados como um array, sendo o primeiro (argv[0]) sempre tendo o nome do arquivo (.py) que é executado
	temp = argv[1]

# No caso de erro seta a variável para texto vazio
except:
	temp = ''

# Realiza uma consulta de terminal, na pasta onde foram salvas as imagens, e joga saída para variável
lista = run(['ls', '-t', atalho], stderr=PIPE, stdout=PIPE)

# Converte os dados da pesquisa em texto e transforma em um array, com o indicador de quebra de linha como final do texto ("\n")
lista = lista.stdout.decode('utf-8').split('\n')

# Loop que percorre o array de impressoras
for i in imp:

	# Loop localiza a primeira ocorrência no array de prints que contém o nome da impressora informada antes
	for j in lista:

		# Se o nome da impressora estiver no nome do arquivo, ele é acrescentado na variável e para o próximo nome de impressora
		if i in j:

			# Variável que recebe o atalho da pasta + o nome do arquivo print
			teste.append(atalho + j)

			# Para o loop de localizar impressora e passa para o próximo nome
			break

# Cria uma lista, onde é removido _data.png, ficando somente o caminho do arquivo + nome da impressora + .png
lista = [s.split('_')[0] + '.png' for s in teste]

# Se a variável tiver como texto a letra "s" ou "S" cria uma pasta
if temp.upper() == 'S':

	# Cria pasta no local específico
	run(['mkdir', atalho2])

# Loop percorre o array de prints para envio ou conferência
for i in range(len(teste)):

	# Copia o print, da pasta onde foram salvas as demais, e cola na mesma pasta com o nome sem data
	run(['cp', teste[i], lista[i]])

	# Se a variável tiver como texto a letra "s" ou "S", executa função
	if temp.upper() == 'S':

		# Copia da pasta salva para pasta criada
		run(['cp', teste[i], atalho2])

	# Abre o "Google Chrome" e exibe os prints, para saber se estão certos, para enviar para prestadora
	run(['/usr/bin/google-chrome-stable', '--incognito', lista[i]])
