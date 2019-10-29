# -*- coding: utf-8 -*-

# pretty much taken from:
# http://rosettacode.org/wiki/Averages/Simple_moving_average


from collections import deque

"""
Computes moving or running averages, averages are always floats
MovingAverage in moving_average.py
"""

class MovingAverage():
    def __init__(self, period):
        """
        construct, set the period
        """
        assert period        == int(period) and period > 0, "Period must be an integer >0"
        self.period = period
        self.stream         = deque()    # store the data here
        self.stream.clear()

    # ---------------------------------------------
    def nextVal(self, n):
        """
        add a value to moving average and return a smoothed value
        filling the stream still leaves some issues -- but looks
        like the right way to me
        may be issues on where float() is used
        """
        stream = self.stream

        stream.append(n)    # appends on the right

        streamlength = len(stream)
        if streamlength > self.period:
            stream.popleft()
            streamlength -= 1
        if streamlength == 0:
            self.value    =  0
        else:
            self.value    = sum( stream ) / float( streamlength )

        return self.value

# ---------------------------------------------
if __name__ == '__main__':
    """
    test of moving average
    """
    for period in [3, 5]:

        print ("\nMOVING AVERAGE (class based): PERIOD =", period)
        sma = MovingAverage( period )
        for i in range(1,6):
            print ( "  Next number = %-2g, SMA = %g " % (i, sma.nextVal( float(i))) )

        for i in range(5, 0, -1):
            print ( "  Next number = %-2g, SMA = %g " % (i, sma.nextVal( float(i))) )

        print( "\npulse" )
        sma = MovingAverage( period )
        for i in [1,1,1,1,1,1,5,5,5,5,5,5,1,1,1,1]:
            print( "  Next number = %-2g, SMA = %g " % (i, sma.nextVal( float(i))) )


        print( sma )

# ========================= eof ========================


