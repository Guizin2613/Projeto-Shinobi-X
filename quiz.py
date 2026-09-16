import random


def iniciar_quiz():

    print('=' * 40)
    print('🥷 QUIZ SOBRE NARUTO 🥷')
    print('=' * 40)


    perguntas = [

        {
            "pergunta": "Quem é o protagonista de Naruto?",
            "opcoes": [
                "1 - Sasuke",
                "2 - Naruto",
                "3 - Kakashi",
                "4 - Itachi"
            ],
            "resposta": "2"
        },

        {
            "pergunta": "Qual é o clã do Naruto?",
            "opcoes": [
                "1 - Uchiha",
                "2 - Hyuga",
                "3 - Uzumaki",
                "4 - Nara"
            ],
            "resposta": "3"
        },

        {
            "pergunta": "Qual é o nome do sensei do Time 7?",
            "opcoes": [
                "1 - Jiraiya",
                "2 - Iruka",
                "3 - Kakashi",
                "4 - Guy"
            ],
            "resposta": "3"
        },

        {
            "pergunta": "Qual é o elemento principal do Chidori?",
            "opcoes": [
                "1 - Fogo",
                "2 - Raio",
                "3 - Água",
                "4 - Terra"
            ],
            "resposta": "2"
        },

        {
            "pergunta": "Quem possui o Sharingan?",
            "opcoes": [
                "1 - Uchiha",
                "2 - Akimichi",
                "3 - Aburame",
                "4 - Inuzuka"
            ],
            "resposta": "1"
        },

        {
            "pergunta": "Qual estilo a Guren usa?",
            "opcoes": [
                "1 - Raio",
                "2 - Vento",
                "3 - Cristal",
                "4 - Água"
            ],
            "resposta": "3"
        },

        {
            "pergunta": "Quem é o filho do Naruto?",
            "opcoes": [
                "1 - Kawaki",
                "2 - Boruto",
                "3 - Mitsuki",
                "4 - Shikadai"
            ],
            "resposta": "2"
        },

        {
            "pergunta": "Quem é o pai do Naruto?",
            "opcoes": [
                "1 - Minato",
                "2 - Kabuto",
                "3 - Orochimaru",
                "4 - Hiruzen"
            ],
            "resposta": "1"
        },

        {
            "pergunta": "Quantas caudas a Kurama tem?",
            "opcoes": [
                "1 - 2 caudas",
                "2 - 5 caudas",
                "3 - 0 caudas",
                "4 - 9 caudas"
            ],
            "resposta": "4"
        },

        {
            "pergunta": "Quem são os integrantes do Time 7?",
            "opcoes": [
                "1 - Naruto, Konohamaru e Gaara",
                "2 - Naruto, Sasuke e Moegi",
                "3 - Naruto, Sasuke e Sakura",
                "4 - Naruto, Shikamaru e Temari"
            ],
            "resposta": "3"
        }

    ]


    pontos = 0


    random.shuffle(perguntas)


    print("=" * 40)
    print("🍥 QUIZ SHINOBI X 🍥")
    print("=" * 40)


    perguntas_sorteadas = random.sample(perguntas, 5)


    for numero, pergunta in enumerate(perguntas_sorteadas, 1):

        print(f"\nPergunta {numero}/5")

        print(pergunta["pergunta"])


        for opcao in pergunta["opcoes"]:

            print(opcao)


        resposta = input("Resposta: ")


        if resposta == pergunta["resposta"]:

            print("✅ ACERTOU! +1 ponto")

            pontos += 1

        else:

            print("❌ ERROU!")


    print("\n" + "=" * 40)

    print("🏆 RESULTADO FINAL 🏆")

    print("=" * 40)


    print("Você fez", pontos, "pontos de 5!")


    # ==========================================
    # RANK
    # ==========================================

    if pontos == 0:

        print("📚 Rank: ESTUDANTE")

    elif pontos == 1:

        print("🍥 Rank: GENIN")

    elif pontos == 2:

        print("🥷 Rank: CHUNNIN")

    elif pontos == 3:

        print("⚔️ Rank: JONIN")

    elif pontos == 4:

        print("🔥 Rank: HOKAGE")

    elif pontos == 5:

        print("👑 Rank: SHINOBI")


    input("\nPressione ENTER para voltar ao menu...")