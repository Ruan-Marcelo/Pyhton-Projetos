from datetime import datetime
from statistics import mean

from flask import Flask, jsonify, request


app = Flask(__name__)


# Base de dados em memoria para manter o projeto em um unico arquivo.
alunos = {
    "2026001": {
        "matricula": "2026001",
        "nome": "Ana Souza",
        "curso": "Analise e Desenvolvimento de Sistemas",
        "email": "ana.souza@email.com",
        "notas": [8.5, 9.0, 7.8],
    },
    "2026002": {
        "matricula": "2026002",
        "nome": "Carlos Lima",
        "curso": "Sistemas de Informacao",
        "email": "carlos.lima@email.com",
        "notas": [6.0, 7.5, 8.0],
    },
}

disciplinas = {
    "PY101": {
        "codigo": "PY101",
        "nome": "Programacao Python",
        "carga_horaria": 80,
    },
    "BD201": {
        "codigo": "BD201",
        "nome": "Banco de Dados",
        "carga_horaria": 60,
    },
}

matriculas_disciplinas = [
    {"aluno": "2026001", "disciplina": "PY101", "data": "2026-05-27"},
    {"aluno": "2026002", "disciplina": "BD201", "data": "2026-05-27"},
]


def resposta(dados=None, mensagem="Operacao realizada com sucesso", status=200):
    """Padroniza as saidas JSON da API."""
    return jsonify({"mensagem": mensagem, "dados": dados}), status


def validar_campos_obrigatorios(dados, campos):
    campos_ausentes = [campo for campo in campos if campo not in dados or dados[campo] in ("", None)]
    if campos_ausentes:
        return f"Campos obrigatorios ausentes: {', '.join(campos_ausentes)}"
    return None


def calcular_media(notas):
    if not notas:
        return 0
    return round(mean(notas), 2)


def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperacao"
    return "Reprovado"


def aluno_com_resultado(aluno):
    media = calcular_media(aluno.get("notas", []))
    aluno_processado = aluno.copy()
    aluno_processado["media"] = media
    aluno_processado["situacao"] = definir_situacao(media)
    return aluno_processado


@app.get("/")
def home():
    return resposta(
        {
            "sistema": "API REST de Gerenciamento Academico",
            "biblioteca": "Flask",
            "rotas": [
                "GET /alunos",
                "POST /alunos",
                "GET /alunos/<matricula>",
                "PUT /alunos/<matricula>",
                "DELETE /alunos/<matricula>",
                "GET /disciplinas",
                "POST /disciplinas",
                "POST /matriculas",
                "GET /relatorio",
            ],
        },
        "API em funcionamento",
    )


@app.get("/alunos")
def listar_alunos():
    return resposta([aluno_com_resultado(aluno) for aluno in alunos.values()])


@app.post("/alunos")
def cadastrar_aluno():
    dados = request.get_json(silent=True) or {}
    erro = validar_campos_obrigatorios(dados, ["matricula", "nome", "curso", "email"])
    if erro:
        return resposta(None, erro, 400)

    matricula = str(dados["matricula"])
    if matricula in alunos:
        return resposta(None, "Ja existe aluno com essa matricula", 409)

    notas = dados.get("notas", [])
    if not isinstance(notas, list) or any(not isinstance(nota, (int, float)) for nota in notas):
        return resposta(None, "O campo notas deve ser uma lista de numeros", 400)

    alunos[matricula] = {
        "matricula": matricula,
        "nome": dados["nome"],
        "curso": dados["curso"],
        "email": dados["email"],
        "notas": notas,
    }
    return resposta(aluno_com_resultado(alunos[matricula]), "Aluno cadastrado com sucesso", 201)


@app.get("/alunos/<matricula>")
def buscar_aluno(matricula):
    aluno = alunos.get(matricula)
    if not aluno:
        return resposta(None, "Aluno nao encontrado", 404)
    return resposta(aluno_com_resultado(aluno))


@app.put("/alunos/<matricula>")
def atualizar_aluno(matricula):
    aluno = alunos.get(matricula)
    if not aluno:
        return resposta(None, "Aluno nao encontrado", 404)

    dados = request.get_json(silent=True) or {}
    for campo in ["nome", "curso", "email"]:
        if campo in dados:
            aluno[campo] = dados[campo]

    if "notas" in dados:
        if not isinstance(dados["notas"], list) or any(
            not isinstance(nota, (int, float)) for nota in dados["notas"]
        ):
            return resposta(None, "O campo notas deve ser uma lista de numeros", 400)
        aluno["notas"] = dados["notas"]

    return resposta(aluno_com_resultado(aluno), "Aluno atualizado com sucesso")


@app.delete("/alunos/<matricula>")
def remover_aluno(matricula):
    if matricula not in alunos:
        return resposta(None, "Aluno nao encontrado", 404)

    aluno_removido = alunos.pop(matricula)
    matriculas_disciplinas[:] = [
        item for item in matriculas_disciplinas if item["aluno"] != matricula
    ]
    return resposta(aluno_removido, "Aluno removido com sucesso")


@app.get("/disciplinas")
def listar_disciplinas():
    return resposta(list(disciplinas.values()))


@app.post("/disciplinas")
def cadastrar_disciplina():
    dados = request.get_json(silent=True) or {}
    erro = validar_campos_obrigatorios(dados, ["codigo", "nome", "carga_horaria"])
    if erro:
        return resposta(None, erro, 400)

    codigo = str(dados["codigo"]).upper()
    if codigo in disciplinas:
        return resposta(None, "Ja existe disciplina com esse codigo", 409)

    try:
        carga_horaria = int(dados["carga_horaria"])
    except (TypeError, ValueError):
        return resposta(None, "A carga horaria deve ser numerica", 400)

    disciplinas[codigo] = {
        "codigo": codigo,
        "nome": dados["nome"],
        "carga_horaria": carga_horaria,
    }
    return resposta(disciplinas[codigo], "Disciplina cadastrada com sucesso", 201)


@app.post("/matriculas")
def matricular_aluno_em_disciplina():
    dados = request.get_json(silent=True) or {}
    erro = validar_campos_obrigatorios(dados, ["aluno", "disciplina"])
    if erro:
        return resposta(None, erro, 400)

    matricula_aluno = str(dados["aluno"])
    codigo_disciplina = str(dados["disciplina"]).upper()

    if matricula_aluno not in alunos:
        return resposta(None, "Aluno nao encontrado", 404)
    if codigo_disciplina not in disciplinas:
        return resposta(None, "Disciplina nao encontrada", 404)

    ja_matriculado = any(
        item["aluno"] == matricula_aluno and item["disciplina"] == codigo_disciplina
        for item in matriculas_disciplinas
    )
    if ja_matriculado:
        return resposta(None, "Aluno ja matriculado nessa disciplina", 409)

    nova_matricula = {
        "aluno": matricula_aluno,
        "disciplina": codigo_disciplina,
        "data": datetime.now().strftime("%Y-%m-%d"),
    }
    matriculas_disciplinas.append(nova_matricula)
    return resposta(nova_matricula, "Matricula realizada com sucesso", 201)


@app.get("/relatorio")
def gerar_relatorio():
    alunos_processados = [aluno_com_resultado(aluno) for aluno in alunos.values()]
    medias = [aluno["media"] for aluno in alunos_processados]

    relatorio = {
        "total_alunos": len(alunos),
        "total_disciplinas": len(disciplinas),
        "total_matriculas": len(matriculas_disciplinas),
        "media_geral": round(mean(medias), 2) if medias else 0,
        "aprovados": sum(1 for aluno in alunos_processados if aluno["situacao"] == "Aprovado"),
        "recuperacao": sum(1 for aluno in alunos_processados if aluno["situacao"] == "Recuperacao"),
        "reprovados": sum(1 for aluno in alunos_processados if aluno["situacao"] == "Reprovado"),
    }
    return resposta(relatorio, "Relatorio academico gerado com sucesso")


if __name__ == "__main__":
    app.run(debug=True)
