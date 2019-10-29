# -*- coding: utf-8 -*-

import  math
import  random

# ========================== Begin Class ================================
class SensorSim:
    """
    simulator for a noisy sensor
    returns a simulated time and sensor reading
    """
    def __init__(self, amplitude, noise_amp, delta_t ):

        self.version        = "2016 01 29.4"

        self.amplitude     = amplitude
        self.noise_amp     = noise_amp
        self.delta_t       = delta_t
        self.time          = 0

    # ------------------------------------------------
    def get_next_sample( self ):
        """
        return tuple ( time, signal )
        """
        signal = self.amplitude * math.sin( self.time ) + ( self.noise_amp ) * random.normalvariate( 0, 1. )

        #signal = ( self.noise_amp/100.) * random.normalvariate( 0, 1. )
        #signal =  random.normalvariate( 0, 1. )

        self.time    += self.delta_t
        return ( self.time, signal )

# ================= eof ============================