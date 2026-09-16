#========================================
#          PROJECT SHINOBI X
#========================================

from criador_ninja import criar_ninja
from gerador_jutsus import gerar_jutsu
from quiz import iniciar_quiz

while True:

    print('=' * 40)
    print('🍥 PROJECT SHINOBI X 🍥')
    print('=' * 40)
    print('1 - Criar Ninja')
    print('2 - Gerador de Jutsus')
    print('3 - Quiz Naruto')
    print('4 - Sair')
    print('=' * 40)

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        criar_ninja()

    elif opcao == '2': 
        gerar_jutsu()

    elif opcao == '3':
        iniciar_quiz()

    elif opcao == '4':
        print('\nAté logo, Shinobi!')
        break

    else:
        print('\nOpção inválida!\n')

