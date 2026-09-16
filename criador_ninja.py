def criar_ninja():

    print("=" * 40)
    print("🥷 CRIADOR NINJA 🥷")
    print("=" * 40)

    nome = input("Nome do ninja: ")

    print("\nEscolha sua vila:")
    print("1 - Konoha")
    print("2 - Areia")
    print("3 - Névoa")
    print("4 - Pedra")
    print("5 - Nuvem")

    escolha_vila = input("Digite o número da vila: ")

    while escolha_vila != "1" and escolha_vila != "2" and escolha_vila != "3" and escolha_vila != "4" and escolha_vila != "5":

        print("\nOpção inválida!")
        escolha_vila = input("Digite novamente: ")

    if escolha_vila == "1":
        vila = "Konoha"

    elif escolha_vila == "2":
        vila = "Areia"

    elif escolha_vila == "3":
        vila = "Névoa"

    elif escolha_vila == "4":
        vila = "Pedra"

    elif escolha_vila == "5":
        vila = "Nuvem"

    print("\nEscolha seu clã:")
    print("1 - Uchiha")
    print("2 - Hyuga")
    print("3 - Uzumaki")
    print("4 - Nara")
    print("5 - Senju")
    print("6 - Outro")

    escolha_cla = input("Clã: ")

    while escolha_cla != "1" and escolha_cla != "2" and escolha_cla != "3" and escolha_cla != "4" and escolha_cla != "5" and escolha_cla != "6":

        print("\nOpção inválida!")
        escolha_cla = input("Digite novamente: ")

    if escolha_cla == "1":
        cla = "Uchiha"

    elif escolha_cla == "2":
        cla = "Hyuga"

    elif escolha_cla == "3":
        cla = "Uzumaki"

    elif escolha_cla == "4":
        cla = "Nara"

    elif escolha_cla == "5":
        cla = "Senju"

    elif escolha_cla == "6":
        cla = input("Digite o nome do clã: ")
    print("\nEscolha seu elemento: ")
    print("1 - Fogo")
    print("2 - Água")
    print("3 - Raio")
    print("4 - Vento")
    print("5 - Terra")
    print("6 - Cristal")

    escolha_elemento = input("Digite o número do elemento: ")

    while escolha_elemento != "1" and escolha_elemento != "2" and escolha_elemento != "3" and escolha_elemento != "4" and escolha_elemento != "5" and escolha_elemento != "6":

        print("\nOpção inválida!")
        escolha_elemento = input("Digite novamente: ")

    if escolha_elemento == "1":
        elemento = "Fogo"

    elif escolha_elemento == "2":
        elemento = "Água"

    elif escolha_elemento == "3":
        elemento = "Raio"

    elif escolha_elemento == "4":
        elemento = "Vento"

    elif escolha_elemento == "5":
        elemento = "Terra"

    elif escolha_elemento == "6":
        elemento = "Cristal"
    classificacao = "Genin"

    print()
    print("=" * 40)
    print("NINJA CRIADO COM SUCESSO!")
    print("=" * 40)

    print("Nome: {}".format(nome))
    print("Vila: {}".format(vila))
    print("Clã: {}".format(cla))
    print("Elemento: {}".format(elemento))
    print("Classificação: {}".format(classificacao))

    print("=" * 40)

    print()
    print("{} {} acaba de iniciar sua jornada ninja!".format(nome, cla))
    print("Boa sorte em sua missão!")

    input("\nPressione ENTER para voltar ao menu...")