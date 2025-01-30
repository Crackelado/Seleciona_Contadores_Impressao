#! python3.10

from subprocess import run, PIPE
from datetime import datetime
from sys import argv

atalho = '/home/usuario/Downloads/'
atalho2 = '/home/usuario/Documents/Luiz2023/CopyUai/' + datetime.now().strftime('%y.%m.%d')
imp = ['ZEQYBQAF4000CFW', 'ZEQYBQAF5001FLM', 'ZDDPB07K110ZF4Y', 'ZEQYBQAF6001RZL', 'ZDDPB07MA174KBW', '6TB443854']
teste = []

try:
      temp = argv[1]
except:
      temp = ''    

lista = run(['ls', '-t', atalho], stderr=PIPE, stdout=PIPE)
lista = lista.stdout.decode('utf-8').split('\n')

for i in imp:
	for j in lista:
		if i in j:
			teste.append(atalho + j)
			break
            
lista = [s.split('_')[0] + '.png' for s in teste]

if temp.upper() == 'S':
    run(['mkdir', atalho2])

for i in range(len(teste)):
    run(['cp', teste[i], lista[i]])

    if temp.upper() == 'S':
        run(['cp', teste[i], atalho2])

    run(['/usr/bin/google-chrome-stable', '--incognito', lista[i]])
