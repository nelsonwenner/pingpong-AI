import numpy as np
from DB_RedeNeural import *
from DB_PingPong import *


class NeuralNetwork:
    def __init__(self, 
        quantidade_entradas, quantidade_neuronios, 
        quantidade_saida, entradas_conjunto_treinamento, 
        saidas_conjunto_treinamento, pesos_sinapticos_w1, 
        pesos_sinapticos_w2, gravar_dados, epocas):
        self.controle_dados_RedeNeural = criando_repositorio_dados_RedeNeural()
        self.entradas_conjunto_treinamento = entradas_conjunto_treinamento
        self.saidas_conjunto_treinamento = saidas_conjunto_treinamento
        self.permissao_gravar_dados = gravar_dados
        self.quantidade_entradas = quantidade_entradas
        self.quantidade_neuronios = quantidade_neuronios
        self.quantidade_saida = quantidade_saida
        self.pesos_sinapticos_w1 = pesos_sinapticos_w1
        self.pesos_sinapticos_w2 = pesos_sinapticos_w2
        self.taxa_aprendizagem = 0.00001
        self.epocas = epocas
     
    # Verificando se existem um DB de pesos a serem utilizados, ou criamos aleatoriamente.
    def verificando_pesos(self):
        if self.pesos_sinapticos_w1 == None:
            self.pesos_sinapticos_w1 = 2 * np.random.random((self.quantidade_entradas, self.quantidade_neuronios)) - 1
        else:
            self.pesos_sinapticos_w1 = np.array(self.pesos_sinapticos_w1)

        if self.pesos_sinapticos_w2 == None:
            self.pesos_sinapticos_w2 = 2 * np.random.random((self.quantidade_neuronios, self.quantidade_saida)) - 1
        else:
            self.pesos_sinapticos_w2 = np.array(self.pesos_sinapticos_w2)

    # Gravando pesos
    def gravando_dados_em_TXT(self):
        if self.permissao_gravar_dados:
            criar_arquivoTXT_IA("peso-w1.txt")
            criar_arquivoTXT_IA("peso-w2.txt")
            guardar_dados_arquivoTXT_IA(self.pesos_sinapticos_w1, "peso-w1.txt")
            guardar_dados_arquivoTXT_IA(self.pesos_sinapticos_w2, "peso-w2.txt")

    # A função Sigmoide, que descreve uma curva em forma de S.
    # Nós passamos a soma ponderada das entradas através desta função para
    # normalize-os entre 0 e 1.
    def sigmoid(self, entrada):
        return 1 / (1 + np.exp(-entrada))

    # A derivada da função Sigmoid.
    # Este é o gradiente da curva sigmóide.
    # Indica que estamos confiantes sobre o peso existente.
    def sigmoid_derivada(self, sigmoid):
        return sigmoid * (1 - sigmoid)

    # Somando para frente
    def somando_para_frente(self, entrada):
        self.resultado_soma_camada_entrada_eOCULTA = self.sigmoid(np.dot(entrada, self.pesos_sinapticos_w1))
        self.resultado_soma_OCULTA_ecamadaSaida = self.sigmoid(np.dot(self.resultado_soma_camada_entrada_eOCULTA, self.pesos_sinapticos_w2))

    # Delta saida
    def delta_saida(self):
        deltaDerivadaSaida = self.taxa_de_error_simples() * self.sigmoid_derivada(self.resultado_soma_OCULTA_ecamadaSaida)
        return deltaDerivadaSaida

    # Delta camada oculta
    def delta_camadaOculta(self):
        deltaCamaOculta = np.dot((self.taxa_de_error_simples()) * self.sigmoid_derivada(self.resultado_soma_OCULTA_ecamadaSaida), self.pesos_sinapticos_w2.T)
        return deltaCamaOculta

    # Taxa simples de error
    def taxa_de_error_simples(self):
        return self.saidas_conjunto_treinamento - self.resultado_soma_OCULTA_ecamadaSaida

    # Propagando o ajuste de pesos
    def Backpropagation(self, camadaEntrada):
        ajustar_peso_w1 = np.dot(camadaEntrada.T, (self.delta_camadaOculta() * self.sigmoid_derivada(self.resultado_soma_camada_entrada_eOCULTA)))
        self.pesos_sinapticos_w1 += (ajustar_peso_w1 * self.taxa_aprendizagem)

        ajustar_peso_w2 = np.dot(self.resultado_soma_camada_entrada_eOCULTA.T, self.delta_saida())
        self.pesos_sinapticos_w2 += (ajustar_peso_w2 * self.taxa_aprendizagem)

    # Metodo para ser usado no jogo, para calcular o DB
    # para que possa resultar se a barrinha vai pra esquerda
    # ou vai para direita de acordo com a condição  se
    # resultado < 0.5 vai ser igual a 0 e a barrinha vai para esquerda
    # se for maior que 0.5 que no caso é 50% vai para a direita.
    def resultado_saida(self, entrada):
        self.somando_para_frente(entrada)
        return self.resultado_soma_OCULTA_ecamadaSaida

    # Nós treinamos a rede neural através de um processo de tentativa e erro.
    # Ajustando os pesos sinápticos a cada vez.
    def treinamento(self):

        # instancie o conjunto de treinamento através da nossa rede neural.
        camadaEntrada = self.entradas_conjunto_treinamento
        self.somando_para_frente(camadaEntrada)

        # Error da rede neural, metodos Mean square error (MSE)
        self.error = np.sum((self.saidas_conjunto_treinamento - self.resultado_soma_OCULTA_ecamadaSaida) ** 2) / len(self.entradas_conjunto_treinamento)

        # Media do error.
        self.media_error = np.mean(np.abs(self.error))

        # Ajustando os pesos de acordo com o error da rede.
        self.Backpropagation(camadaEntrada)

        self.gravando_dados_em_TXT()

        print("Media error: {:.2f} %".format(self.media_error))


if __name__ == '__main__':

    input = np.array(input("dados-55.txt"))
    output = np.array(output("dados-55.txt"))

    w1 = None

    w2 = None

    salvar_pesos = False

    IA = NeuralNetwork(2, 30, 1, input, output, w1, w2, salvar_pesos, 100000)

    IA.verificando_pesos()

    cont = 0

    while cont < IA.epocas:

        IA.treinamento()

        cont += 1
