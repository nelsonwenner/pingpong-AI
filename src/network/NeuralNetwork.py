from sys import path
path.append('..')
from database.controller.db import *
import numpy as np


class NeuralNetwork:
    def __init__(self,
        amount_entry, amount_neurons,
        amount_output, entry_set_training,
        output_set_training, weight_synaptic_w1,
        weight_synaptic_w2, permission_save, epoch):
        self.entry_set_training = entry_set_training
        self.output_set_training = output_set_training
        self.permission_save = permission_save
        self.amount_entry = amount_entry
        self.amount_neurons = amount_neurons
        self.amount_output = amount_output
        self.weight_synaptic_w1 = weight_synaptic_w1
        self.weight_synaptic_w2 = weight_synaptic_w2
        self.rate_learning = 0.00001
        self.epoch = epoch

    '''
    Verificando se existem um DB de pesos a serem utilizados, ou criamos aleatoriamente.
    
    '''
    def checking_exists_weights(self):
        if self.weight_synaptic_w1 == None:
            self.weight_synaptic_w1 = 2 * np.random.random((self.amount_entry, self.amount_neurons)) - 1
        else:
            self.weight_synaptic_w1 = np.array(self.weight_synaptic_w1)

        if self.weight_synaptic_w2 == None:
            self.weight_synaptic_w2 = 2 * np.random.random((self.amount_neurons, self.amount_output)) - 1
        else:
            self.weight_synaptic_w2 = np.array(self.weight_synaptic_w2)

    '''
    Gravando pesos
    
    '''
    def recording_data(self):
        if self.permission_save:
            create_file('/../database/weights/', 'weight-w1.txt')
            create_file('/../database/weights/', 'weight-w2.txt')
            save_data('/../database/weights/', self.weight_synaptic_w1, 'weight-w1.txt')
            save_data('/../database/weights/', self.weight_synaptic_w2, 'weight-w2.txt')

    '''
     A função Sigmoide, que descreve uma curva em forma de S.
     Nós passamos a soma ponderada das entradas através desta função para
     normalize-os entre 0 e 1.
     
    '''
    def sigmoid(self, entry):
        return np.exp(np.fmin(entry, 0)) / (1 + np.exp(-np.abs(entry)))

    '''
     A derivada da função Sigmoid.
     Este é o gradiente da curva sigmóide.
     Indica que estamos confiantes sobre o peso existente.
     
    '''
    def sigmoid_derivada(self, sigmoid):
        return sigmoid * (1 - sigmoid)

    '''
     Somando para frente
    '''
    def sum_feed_forward(self, entry):
        self.result_sum_hidden_input_layer = self.sigmoid(np.dot(entry, self.weight_synaptic_w1))
        self.result_sum_hidden_output_layer = self.sigmoid(np.dot(self.result_sum_hidden_input_layer, self.weight_synaptic_w2))

    '''
     Delta saida
    
    '''
    def delta_output(self):
        return self.simple_error_rate() * self.sigmoid_derivada(self.result_sum_hidden_output_layer)

    '''
     Delta camada oculta
    
    '''
    def delta_layer_hidden(self):
        return np.dot((self.simple_error_rate()) * self.sigmoid_derivada(self.result_sum_hidden_output_layer), self.weight_synaptic_w2.T)

    '''
     Taxa simples de error
    
    '''
    def simple_error_rate(self):
        return self.output_set_training - self.result_sum_hidden_output_layer

    '''
     Propagando o ajuste de pesos
    
    '''
    def backpropagation(self, input_layer):
        adjust_weight_w1 = np.dot(input_layer.T, (self.delta_layer_hidden() * self.sigmoid_derivada(self.result_sum_hidden_input_layer)))
        self.weight_synaptic_w1 += (adjust_weight_w1 * self.rate_learning)

        adjust_weight_w2 = np.dot(self.result_sum_hidden_input_layer.T, self.delta_output())
        self.weight_synaptic_w2 += (adjust_weight_w2 * self.rate_learning)

    '''
     Metodo para ser usado no jogo, para calcular o DB
     para que possa resultar se a barrinha vai pra esquerda
     ou vai para direita de acordo com a condição  se
     resultado < 0.5 vai ser igual a 0 e a barrinha vai para esquerda
     se for maior que 0.5 que no caso é 50% vai para a direita.
    
    '''
    def result_output(self, entry):
        self.sum_feed_forward(entry)
        return self.result_sum_hidden_output_layer

    '''
     Nós treinamos a rede neural através de um processo de tentativa e erro.
     Ajustando os pesos sinápticos a cada vez.
    
    '''
    def training(self):

        '''
         instancie o conjunto de treinamento através da nossa rede neural.

        '''
        input_layer = self.entry_set_training
        self.sum_feed_forward(input_layer)

        '''
         Error da rede neural, metodos Mean square error (MSE)
        
        '''
        self.error = np.sum((self.output_set_training - self.result_sum_hidden_output_layer) ** 2) / len(self.entry_set_training)

        '''
         Media do error.
        
        '''
        self.mean_error = np.mean(np.abs(self.error))

        '''
         Ajustando os pesos de acordo com o error da rede.
        
        '''
        self.backpropagation(input_layer)

        self.recording_data()

        print("Mean error: {:.2f} %".format(self.mean_error))


if __name__ == '__main__':

    input = np.array(get_data('/../database/data/data-94.txt', 0))
    output = np.array(get_data('/../database/data/data-94.txt', 1))

    w1 = None

    w2 = None

    save_weights = True

    IA = NeuralNetwork(2, 30, 1, input, output, w1, w2, save_weights, 100000)

    IA.checking_exists_weights()

    cont = 0

    while cont < IA.epoch:

        IA.training()

        cont += 1
    