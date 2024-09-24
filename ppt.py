'''
Jogo do Pedra-Papel-Tesoura
2024.08.13
Gustavo Alves Hanisch
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep

# Constantes, Variaveis e Listas
msgsInicio = ['Seja bem vind@ ao',
             'Jogo do PEDRA-PAPEL-TESOURA',
             'desenvolvido por: Gustavo Alves',
             'BOA SORTE!!!']
msgs = []
playAgain = ''
playerScore = 0
computerScore = 0

# Funções
def startPPT():
  while(True):
    clrScreen()
    displayHeader(msgsInicio)
    playPPT()
    # função para começar o jogo
    playAgain = getUserOption('Deseja jogar novamente?[s/n]')
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N', 'y', 'Y']): # quando a resposta digitada for invalida, ele ira perguntar novamente, ate a resposta certa for digitada
      playAgain = getUserOption('Deseja jogar novamente?[s/n]')
    if playAgain.lower() != 's':
      break


def displayMenu():
  msgs = ['Escolha:', '[0] --> Pedra', '[1] --> Papel', '[2] --> Tesoura']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()
def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerUserChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'empate!'
  elif (playerChoice == '0' and computerChoice == '2') or (playerChoice == '1' and computerChoice == '0') or (playerChoice == '2' and computerChoice == '1' ):
    play = f"{playerChoice} vence {computerChoiceStr}"
    result = 'Voce Ganhou!'
  else:
    play = f"{computerChoice} vence {playerChoice}"
    result = 'Voce Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoice,
         'Jogada do PC: ' + computerChoiceStr,
         play, result]
  displayHeader(msgs)
  return result

def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0', '1', '2']):
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
    sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Que pena','YOU LOSE!'])

# Main


























































































































































