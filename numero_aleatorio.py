from random import randint

nome = input('Olá, qual é seu nome? ')
print(f'Ok! {nome}, estou escolhendo um número de 1 a 10. Você consegue adivinhar qual? Você terá 3 tentativas. ')

numero_adivinhado = randint(1,10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas +1):
    numero_escolhido = int(input('Escolha um número: '))
    if numero_escolhido == numero_adivinhado:
        print(f'Parabéns! Você acertou em {tentativa}, tentativas!')
        break
    elif numero_escolhido > numero_adivinhado:
        print('Escolha um número menor!')
    else:
        print('Escolha um número maior!')
print(f'O número adivinhado era {numero_adivinhado}. Obrigado por jogar!')