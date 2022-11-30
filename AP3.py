print('Seja muito bem vindo ao MEGA QUIZ!')
print('Importante: não se esqueça de digitar as respostas com letras maiúsculas.')
resposta_usuario = input('\nDeseja iniciar o jogo? (S/N): ')

if resposta_usuario != 'S':
    quit()

ponto = 0

print('\nIniciando...')
print('\nO que é um pixel? \n')
print('(A) Um filme do Adam Sandler.')
print('(B) Um ponto luminoso que, juntamente de outros do mesmo tipo, forma imagens na tela.')
print('(C) Um animal raro.')
resposta_1 = input("Resposta: ")

if resposta_1 == "B":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nQual dessas linguagens não é uma linguagem-front end? \n')
print('(A) Python.')
print('(B) HTML.')
print('(C) CSS.')
resposta_2 = input('Resposta: ')

if resposta_2 == "A":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nO que é um software? \n')
print('(A) Conjunto de componentes lógicos de um computador.')
print('(B) Equipamento mecânico necessário para a realização de uma atividade.')
print('(C) Pequeno ventilador que refrigera ou ajuda a refrigerar um motor.')
resposta_3 = input('Resposta: ')

if resposta_3 == "A":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nO que é um hardware? \n')
print('(A) Conjunto de componentes lógicos de um computador.')
print('(B) É um Transformer.')
print('(C) Equipamento mecânico necessário para a realização de uma atividade.')
resposta_4 = input('Resposta: ')

if resposta_4 == "C":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nO que é a programação? \n')
print('(A) Dar aulas em uma escola.')
print('(B) Processo de escrita, testes e manutenção de programas.')
print('(C) Programação é adestrar um cão.')
resposta_5 = input('Resposta: ')

if resposta_5 == "B":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nO que é a linguagem SQL? \n')
print('(A) Idioma mãe dos Astecas.')
print('(B) Linguagem padrão para trabalhar com bancos de dados relacionais.')
print('(C) É o ato de fazer mímicas.')
resposta_6 = input('Resposta: ')

if resposta_6 == "B":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nQual das linguagens abaixo foi criada em 1972? \n')
print('(A) C.')
print('(B) Latim.')
print('(C) TypeScript.')
resposta_7 = input('Resposta: ')

if resposta_7 == "A":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!')

print('\nO que é um site? \n')
print('(A) É um aplicativo de namoro.')
print('(B) Local físico de encontro de programadores.')
print('(C) Conjunto de páginas web.')
resposta_8 = input('Resposta: ')

if resposta_8 == "C":
    print('Acertou!')
    ponto = ponto + 1
else:
    print('Errou!\n')

print('XXXXX'*30)
print('\nQuiz encerrado.')
print(f'Pontuação: {ponto}/8')