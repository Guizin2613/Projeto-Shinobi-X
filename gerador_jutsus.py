def gerar_jutsu(): 

    print('=' * 40)
    print('🥷 GERADOR DE JUTSUS 🥷')
    print('=' * 40)

    nome = input('Nome do Jutsu: ')
    print('\nEscolha o elemento: ')
    print('1 - Fogo')
    print('2 - Água')
    print('3 - Raio')
    print('4 - Vento')
    print('5 - Terra')
    print('6 - Cristal')

    elemento = input('\nElemento: ')
    
    if elemento == '1':
        elemento = 'Fogo'
    elif elemento == '2':
        elemento = 'Água'
    elif elemento == '3':
        elemento = 'Raio'
    elif elemento == '4':
        elemento = 'Vento'
    elif elemento == '5':
        elemento = 'Terra'
    elif elemento == '6':
        elemento = 'Cristal'    
    else:
        elemento = 'Desconhecido'    

    print()
    print('=' * 40)
    print('JUTSU CRIADO!')
    print('=' * 40)

    print('ESTILO {}: {}'.format(elemento.upper(), nome.upper()))

    input('\nPressione ENTER para voltar ao menu...')