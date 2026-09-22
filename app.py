from flask import Flask, render_template, request, session, redirect, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import random
import os


app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY','project_shinobi_X')

usuarios = {}


# ==========================================================
# CADASTRO
# ==========================================================

@app.route(
    "/cadastro",
    methods=["GET", "POST"]
)
def cadastro():

    if request.method == "POST":

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        if usuario in usuarios:

            return "Usuário já existe!"

        senha_hash = generate_password_hash(senha)

        usuarios[usuario] = senha_hash

        return redirect("/login")

    return render_template(
        "cadastro.html"
    )


# ==========================================================
# LOGIN
# ==========================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        if usuario not in usuarios:

            return "Usuário ou senha incorretos!"

        senha_hash = usuarios[usuario]

        if check_password_hash(
            senha_hash,
            senha
        ):

            session["usuario"] = usuario

            return redirect("/")

        return "Usuário ou senha incorretos!"

    return render_template(
        "login.html"
    )


# ==========================================================
# LOGOUT
# ==========================================================

@app.route("/logout")
def logout():

    session.pop(
        "usuario",
        None
    )

    return redirect("/login")

# ==========================================================
# PERGUNTAS DO QUIZ
# ==========================================================

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


# ==========================================================
# IMAGENS DOS JUTSUS
# ==========================================================

imagens_jutsus = {

    "dragao_cristalizado": "dragao_cristalizado.png",

    "dragao_fogo": "dragao_fogo.png",
    "dragao_agua": "dragao_agua.png",
    "dragao_raio": "dragao_raio.png",
    "dragao_vento": "dragao_vento.png",
    "dragao_terra": "dragao_terra.png",

    "furacao": "furacao.png",
    "tornado": "tornado.png",

    "onda": "onda.png",
    "tsunami": "tsunami.png",

    "chama": "chama.png",
    "explosao": "explosao.png",

    "trovao": "trovao.png",
    "relampago": "relampago.png",

    "terremoto": "terremoto.png",
    "rocha": "rocha.png",

    "elemento_fogo": "elemento_fogo.png",
    "elemento_agua": "elemento_agua.png",
    "elemento_raio": "elemento_raio.png",
    "elemento_vento": "elemento_vento.png",
    "elemento_terra": "elemento_terra.png",
    "elemento_cristal": "elemento_cristal.png"

}


# ==========================================================
# ESCOLHER IMAGEM
# ==========================================================

def escolher_imagem_jutsu(nome, elemento):

    nome_formatado = nome.lower()

    nome_formatado = (
        nome_formatado
        .replace("á", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("à", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )

    elemento_formatado = elemento.lower()

    elemento_formatado = (
        elemento_formatado
        .replace("á", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("à", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )


    # ======================================================
    # DRAGÃO
    # ======================================================

    if "dragao" in nome_formatado:

        if elemento_formatado == "cristal":
            return "dragao_cristalizado.png"

        elif elemento_formatado == "fogo":
            return "dragao_fogo.png"

        elif elemento_formatado == "agua":
            return "dragao_agua.png"

        elif elemento_formatado == "raio":
            return "dragao_raio.png"

        elif elemento_formatado == "vento":
            return "dragao_vento.png"

        elif elemento_formatado == "terra":
            return "dragao_terra.png"


    # ======================================================
    # PALAVRAS ESPECÍFICAS
    # ======================================================

    palavras = {

        "furacao": "furacao.png",
        "tornado": "tornado.png",

        "onda": "onda.png",
        "tsunami": "tsunami.png",

        "chama": "chama.png",
        "explosao": "explosao.png",

        "trovao": "trovao.png",
        "relampago": "relampago.png",

        "terremoto": "terremoto.png",
        "rocha": "rocha.png"

    }


    for palavra, imagem in palavras.items():

        if palavra in nome_formatado:

            return imagem


    # ======================================================
    # IMAGEM PADRÃO DO ELEMENTO
    # ======================================================

    return "elemento_" + elemento_formatado + ".png"


# ==========================================================
# SERVIR IMAGENS DOS JUTSUS
# ==========================================================

@app.route("/imagem-jutsu/<nome>")
def imagem_jutsu(nome):

    pasta = os.path.join(
        app.root_path,
        "static",
        "images",
        "jutsus"
    )

    return send_from_directory(
        pasta,
        nome
    )


# ==========================================================
# PÁGINA INICIAL
# ==========================================================

@app.route("/")
def inicio():


    return redirect("/cadastro")

# ==========================================================
# CRIADOR NINJA
# ==========================================================

@app.route(
    "/criador-ninja",
    methods=["GET", "POST"]
)
def criador_ninja():

    if request.method == "POST":

        nome = request.form["nome"]

        vila = request.form["vila"]

        cla = request.form["cla"]

        if cla == "Outro":

            cla = request.form["outro_cla"]

        elemento = request.form["elemento"]


        ninja = {

            "nome": nome,
            "vila": vila,
            "cla": cla,
            "elemento": elemento

        }


        return render_template(
            "ninja_criado.html",
            ninja=ninja
        )


    return render_template(
        "criador_ninja.html"
    )


# ==========================================================
# REGISTRAR NINJA
# ==========================================================

@app.route(
    "/registrar-ninja",
    methods=["POST"]
)
def registrar_ninja():

    ninja = {

        "nome": request.form["nome"],
        "vila": request.form["vila"],
        "cla": request.form["cla"],
        "elemento": request.form["elemento"]

    }


    ninjas = session.get(
        "ninjas",
        []
    )

    ninjas.append(ninja)

    session["ninjas"] = ninjas


    return redirect("/")


# ==========================================================
# APAGAR NINJA
# ==========================================================

@app.route(
    "/apagar-ninja/<int:indice>",
    methods=["POST"]
)
def apagar_ninja(indice):

    ninjas = session.get(
        "ninjas",
        []
    )


    if 0 <= indice < len(ninjas):

        ninjas.pop(indice)


    session["ninjas"] = ninjas


    return redirect("/")


# ==========================================================
# GERADOR DE JUTSUS
# ==========================================================

@app.route(
    "/gerador-jutsu",
    methods=["GET", "POST"]
)
def gerador_jutsu():

    if request.method == "POST":

        nome = request.form["nome"]

        elemento = request.form["elemento"]


        if elemento == "1":

            elemento = "Fogo"

        elif elemento == "2":

            elemento = "Água"

        elif elemento == "3":

            elemento = "Raio"

        elif elemento == "4":

            elemento = "Vento"

        elif elemento == "5":

            elemento = "Terra"

        elif elemento == "6":

            elemento = "Cristal"

        else:

            elemento = "Desconhecido"


        imagem = escolher_imagem_jutsu(
            nome,
            elemento
        )


        return render_template(
            "jutsu_criado.html",
            nome=nome,
            elemento=elemento,
            imagem=imagem
        )


    return render_template(
        "gerador_jutsu.html"
    )


# ==========================================================
# REGISTRAR JUTSU
# ==========================================================

@app.route(
    "/registrar-jutsu",
    methods=["POST"]
)
def registrar_jutsu():

    jutsu = {

        "nome": request.form["nome"],
        "elemento": request.form["elemento"]

    }


    jutsus = session.get(
        "jutsus",
        []
    )

    jutsus.append(jutsu)

    session["jutsus"] = jutsus


    return redirect("/")


# ==========================================================
# APAGAR JUTSU
# ==========================================================

@app.route(
    "/apagar-jutsu/<int:indice>",
    methods=["POST"]
)
def apagar_jutsu(indice):

    jutsus = session.get(
        "jutsus",
        []
    )


    if 0 <= indice < len(jutsus):

        jutsus.pop(indice)


    session["jutsus"] = jutsus


    return redirect("/")


# ==========================================================
# QUIZ
# ==========================================================

@app.route("/quiz")
def quiz():

    perguntas_sorteadas = random.sample(
        perguntas,
        5
    )


    session["quiz_perguntas"] = (
        perguntas_sorteadas
    )


    return render_template(
        "quiz.html",
        perguntas=perguntas_sorteadas
    )


# ==========================================================
# RESULTADO DO QUIZ
# ==========================================================

@app.route(
    "/quiz-resultado",
    methods=["POST"]
)
def quiz_resultado():

    perguntas_quiz = session.get(
        "quiz_perguntas",
        []
    )


    pontos = 0


    for numero, pergunta in enumerate(
        perguntas_quiz
    ):

        resposta_usuario = request.form.get(
            f"pergunta_{numero}"
        )


        if resposta_usuario == pergunta["resposta"]:

            pontos += 1


    if pontos == 0:

        rank = "ESTUDANTE"

        mensagem = (
            "📚 Continue estudando "
            "o caminho ninja!"
        )

    elif pontos == 1:

        rank = "GENIN"

        mensagem = (
            "🍥 Você está começando "
            "sua jornada ninja!"
        )

    elif pontos == 2:

        rank = "CHUNNIN"

        mensagem = (
            "🥷 Você já está evoluindo "
            "bastante!"
        )

    elif pontos == 3:

        rank = "JONIN"

        mensagem = (
            "⚔️ Seu conhecimento ninja "
            "está muito bom!"
        )

    elif pontos == 4:

        rank = "HOKAGE"

        mensagem = (
            "🔥 Você está quase "
            "no nível máximo!"
        )

    else:

        rank = "SHINOBI"

        mensagem = (
            "👑 Você dominou completamente "
            "o Quiz Shinobi!"
        )


    return render_template(
        "quiz_resultado.html",
        pontos=pontos,
        rank=rank,
        mensagem=mensagem
    )


# ==========================================================
# EXECUTAR
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )