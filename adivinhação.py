from random import randint
from time import sleep

print('------------------------------------------')
print('          JOGO DA ADIVINHAÇÃO             ')
print('------------------------------------------')
print('''ESCOLHA O NÍVEL DE DIFICULDADE DO SEU JOGO
[1] FÁCIL
[2] MÉDIO
[3] DIFÍCIL''')
dificuldade = int(input('Digite o número correspondente a dificuldade desejada: '))
tentativas = 0

if dificuldade == 1:
    tentativas = 10
elif dificuldade == 2:
    tentativas = 7
elif dificuldade == 3:
    tentativas = 5
else:
    print('Já que você não quis escolher, vou escolher um número aleatório pra você :D, boa sorte')
    tentativas = randint(5, 10)

resposta = randint(1, 100)


while tentativas >= 0:
    print('O número restante de tentativas é igual a :', tentativas)
    chute = int(input('Tenta adivinhar o número que eu estou pensando entre 1 e 100... '))
    if chute > resposta:
        print('SEU CHUTE FOI ALTO DEMAIS, TENTE UM NÚMERO MENOR')
        tentativas = tentativas - 1
    elif chute < resposta:
        print('SEU CHUTE FOI BAIXO DEMAIS, TENTE UM NÚMERO MAIOR')
        tentativas = tentativas - 1
    else:
        print('PUXA VOCÊ ACERTOU, PARABÉNS!!!!')
        break
    if tentativas == 0 and resposta != chute:
        print('O NÚMERO DE TENTATIVAS ACABARAM...TENTE JOGAR NOVAMENTE')
        print('MAS SÓ PRA SABER, O MEU NÚMERO ESCOLHIDO FOI', resposta)
        break
    

