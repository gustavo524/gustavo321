'''
Arquivo de Modulos
2024.08.13
Gustavo Alves Hanisch
'''

# --> Blibliotecas
from random import choice

# --> Constantes, Vsriaveis e Listas
TAM = 50 # Tamanho da Tela
CAR = choice(['=', '*', '|', '-']) # Caracter utilizado para desenho da tela
MAR = 4 # Tamanho da Margem

# --> Funções
def clrScreen(): # Função para limpar a tela
  print('\n'*TAM) # Mostra na Tela \n == linha * TAM

def displayLine(): # Função para mostrar uma linha de caracteres
  print(CAR*TAM)

def displayMsg(msg): # Mostra uma msg alinhada a esquerda entre CAR
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}')

def displayMsgCenter(msg):
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}')

def displayHeader(msgs):
  displayLine()
  for item in msgs:
    displayMsgCenter(item)
  displayLine()
  
def getUserOption(msg):
  option = input(f'{CAR} {msg}: ').strip()
  return option
                  
def validateUserOption(option, listOptions):
  if option in listOptions:
    return True
  else:
    msgsErro = ['Opção Inválida!', 'Escolha Novamente...']
    displayHeader(msgsErro)
    return False

def displayHeaderT(msgs):
  displayLine()
  for item in msgs:
    displayMsgCenter(item)
    slep(1)
  displayLine()
# --> Main


































































































































































































































