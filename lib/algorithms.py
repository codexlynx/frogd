import time

class Algorithms(object):

    #All dinamic parameters are str()
    def time_based(core, mode, id, minutes):
        if int(id) == core.max: #If it's exceded the maximum number of networks
            id = 0
        elif mode == False: #If no connect
            id = int(id) + 1
        else: #Normal function
            real = int(minutes) * 1#60
            time.sleep(real)
            id = int(id) + 1

        return id
        #You must return int()
