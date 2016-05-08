import time

class Algorithms(object):

    #All parameters are str()
    def time_based(core, id, minutes):
        real = int(minutes) * 1#60
        time.sleep(real)
        if int(id) == core.max:
            id = 0
        else:
            id = int(id) + 1
        return id
        #You must return int()
