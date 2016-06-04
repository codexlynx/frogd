#!/usr/bin/env python

import time

class Algorithms(object):

    #All dinamic parameters are str()
    def time_based(core, connect, id, minutes):
        if connect == False: #If no connect
            id = int(id) + 1
        else:
            #Functional algorithm
            real = int(minutes) * 1#60
            time.sleep(real)
            if int(id) == core.max: #If it's exceded the maximum number of networks
                id = 0
            else:
                id = int(id) + 1 #Normal function

        return id
        #You must return int()
