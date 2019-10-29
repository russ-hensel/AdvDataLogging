# -*- coding: utf-8 -*-

"""
Computes moving or running averages, averages are always floats
DataTrigger in data_trigger.py 
"""

class DataTrigger():
    def __init__(self, trigger_value ):
        """
        construct, set the trigger_value
        """

        self.trigger_value   = trigger_value
        self.last_value      = 0.
        self.data_ix         = -1    # counting the values

    # ---------------------------------------------
    def need_save(self, value ):
        self.data_ix      += 1

        if self.data_ix == 0:
            return True

        if value > ( self.last_value + self.trigger_value ):
            self.last_value = value
            return True

        if value < ( self.last_value - self.trigger_value ):
            self.last_value = value
            return True

# ================= eof ===============

