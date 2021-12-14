#
# Individual.py
#
#
from autochess_sys import *
import math
import random
import numpy as np
class neural_network:
    def __init__(self,network):
        self.weight = []
        self.activations = []
        for layer in network:
            if layer[0] != None:
                input_size = layer[0]
            else:
                input_size = network[network.index(layer) - 1][1]
            output_size = layer[1]
            activation = layer[2]
            self.weights.append(np.random.randn(input_size,output_size))
            self.activations.append(activation)
    def propagate(self,data):
        input_data = data
        for i in range(len(self.weights)):
            z = np.dot(input_data,self.weights[i])
            a = self.activations[i](z)
            input_data = a
        yhat = a
        return yhat
    self.neural_network = neural_network(network)
    self.fitness = 0
class Individual:
    """
    Individual
    """  
    def __init__(self,network):
        self.strength= 0
        chesstypelist = system.chesstypelist
        level = len(chesstypelist)
        types = max(chesstypelist) 
        self.hand_cards = np.zeros((3,level,types))
        self.money = 0
        self.level = 1
        self.fit=None
    def hand_cards(self,chess):
        self.hand_cards[0][chess[0]][chess[1]]+=1
    def refreshtable(self):
        self.money = self.money - 2
        return system.chessoffer(self.level)
                
    def state_check(self):# state_check should be a binary tree
        self.hand_cards[1] = self.hand_cards[0]/3
        self.hand_cards[1] = self.hand_cards[1].astype(int)
        self.hand_cards[1] = self.hand_cards[1].astype(float)
        self.hand_cards[2] = self.hand_cards[1]/3
        self.hand_cards[2] = self.hand_cards[2].astype(int)
        self.hand_cards[2] = self.hand_cards[2].astype(float)
    def choicetime(self, epoch):
        # in a single epoch, a player should go through three part : get money, buying, end epoch
        # buying is the most tricky part of this game, it needs a 'brain'
        money += system.money_offer(self.money, epoch)
        chess_table = system.chessoffer(self.level)
        
        
        
        
