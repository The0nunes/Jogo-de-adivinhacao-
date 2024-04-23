import random

def main():
    print('--- Bem-vindo ao Jogo de Adivinhação ---')
    input('Pressione Enter para iniciar o jogo...')

    jogar_novamente = True

    while jogar_novamente:
        jogar_jogo()

        resposta = input('Deseja jogar novamente? (s/n): ').lower()
        jogar_novamente = resposta == 's'

    print('Obrigado por jogar!')

def jogar_jogo():
    numero_pensado = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = input('Adivinhe o número (de 1 a 100): ')

        try:
            tentativa = int(tentativa)
        except ValueError:
            print('Por favor, digite um número válido.')
            continue

        if tentativa < 1 or tentativa > 100:
            print('O número digitado está fora da faixa permitida.')
            continue

        tentativas += 1

        if tentativa == numero_pensado:
            print(f'Parabéns! Você acertou o número "{numero_pensado}" em {tentativas} tentativas.')
            break
        elif tentativa < numero_pensado:
            print('O número que você está tentando adivinhar é maior.')
        else:
            print('O número que você está tentando adivinhar é menor.')

if __name__ == '__main__':
    main()
