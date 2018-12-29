import os, json


def criando_repositorio_dados_pingpong():
    try:
        caminho = os.getcwd() + "/" + "dados-pingpong"
        os.makedirs(caminho)
    except Exception:
        pass


def criar_arquivoTXT(nome):
    caminho = os.getcwd() + "/" + "dados-pingpong" + "/" + nome
    return open(caminho, "w")


def guardar_arquivoTXT(dados, nome_arquivo):
    caminho = open(os.getcwd() + "/" + "dados-pingpong" + "/" + nome_arquivo + "", "w")
    with caminho as out:
        json.dump(dados, out)


def PingPong_dados_arquivoTXT(nome_arquivo):
    caminho = open(os.getcwd() + "/" + "dados-pingpong" + "/" + nome_arquivo + "")
    dados_entradas = [] + json.load(caminho)
    return dados_entradas


def input(nome_arquivo):
    arquivo = PingPong_dados_arquivoTXT(nome_arquivo)
    x = []
    for item in arquivo:
        x.append(item[0])
    return x


def output(nome_arquivo):
    arquivo = PingPong_dados_arquivoTXT(nome_arquivo)
    x = []
    for item in arquivo:
        x.append(item[1])
    return x


