'''
Projeto Jogo Pedra-Papel-Tesoura e Par ou Ímpar 
2024.08.13
Gustavo Alves Hanisch
'''

# --> Bibliotecas
# Importa funções do arquivo modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption
from ppt import startPPT
from parimpar import startParImpar

# --> Constantes, Variaveis e Listas

# --> Funções

# --> Main
msgs = ['Seja Bem vind@ aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR']
displayHeader(msgs)
msgs = ['Digite 0 --> sair', 'Digite 1 --> Pedra-Papel-Tesoura','Digite 2 --> Par ou Ímpar']
displayHeader(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0', '1', '2']):
  opUser = getUSerOption('Sua escolha')
  if(opUser == '1'):
    startPPT()
  elif(opUser == '2'):
    starParImpar()
  else:
    displayMsg('Até a próxima...')
  
startPPT()










































































































































