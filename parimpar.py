'''
Jogo do Par ou Ímpar
2024.08.20
Gustavo Alves Hanisch
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep

# Constantes, Variaveis e Listas
msgsInicio = ['Seja bem vind@ ao',
             'Jogo do Par ou Ímpar',
             'desenvolvido por: Gustavo Alves',
             'BOA SORTE!!!']
msgs = []
playAgain = ''
playerScore = 0
computerScore = 0

# Funções
def startParImpar():
  while(True):
    clrScreen()
    displayHeader(msgsInicio)
    playParImpar()
    # função para começar o jogo
    playAgain = getUserOption('Deseja jogar novamente?[s/n]')
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N', 'y', 'Y']): # quando a resposta digitada for invalida, ele ira perguntar novamente, ate a resposta certa for digitada
      playAgain = getUserOption('Deseja jogar novamente?[s/n]')
    if playAgain.lower() != 's':
      break


def displayMenu():
  msgs = ['Escolha:', '[1] --> Par', '[2] --> Ímpar']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()
  
def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
  
def determineWinner(playerChoice, playerNumber, computerNumber):
  play = ''
  result = ''
  choices = ['Par', 'Ímpar']
  playerUserChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  total = playerNumber + computerNumber
  if total % 2 == int(playerChoice): 
    result = 'Voce Ganhou!'
  else:
    play = f"{computerChoice} vence {playerChoice}"
    result = 'Voce Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoice,
         'Jogada do PC: ' + computerChoiceStr,
         play, result]
  displayHeader(msgs)
  return result

def playParImpar():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['1', '2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if "Ganhou" in result:
      playerScore += 1 
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
    
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Que pena','YOU LOSE!'])

# Main














































































































































































































































































































































































































































































































































































































































































































































