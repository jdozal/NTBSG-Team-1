#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Entropy: 
    def __init__(self, noUniqueVals, noPackets):
        self.noUniqueVals = noUniqueVals
        self.noPackets = noPackets
    
    def calculateEntropy(self):
        # Number of packets is 0
        if self.noPackets == 0:
            return -1;
        return self.noUniqueVals/self.noPackets
