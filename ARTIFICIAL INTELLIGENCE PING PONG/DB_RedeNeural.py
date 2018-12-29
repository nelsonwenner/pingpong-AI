import os, json


def criando_repositorio_dados_RedeNeural():
    try:
        caminho = os.getcwd() + "/" + "dados-redeneural"
        os.makedirs(caminho)
    except Exception:
        pass


def criar_arquivoTXT_IA(nome):
    caminho = os.getcwd() + "/" + "dados-redeneural" + "/" + nome
    return open(caminho, "w")


def guardar_dados_arquivoTXT_IA(dados, nome_arquivo):
    caminho = open(os.getcwd() + "/" + "dados-redeneural" + "/" + nome_arquivo + "", "w")
    with caminho as out:
        json.dump(dados.tolist(), out)


def IA_dados_arquivoTXT(nome_arquivo):
    caminho = open(os.getcwd() + "/" + "dados-redeneural" + "/" + nome_arquivo + "")
    dados_entradas = [] + json.load(caminho)
    return dados_entradas

