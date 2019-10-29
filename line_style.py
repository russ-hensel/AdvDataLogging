# -*- coding: utf-8 -*-

class LineStyle( object ):
    """
    dispenses row by row a tuple of row style types to
    help make it easy to tell graph lines apart
    use instead of mathplot defaults
    use:
        self.current_style  = self.lineStyle.getStyle()  # ( line, color, marker )
        self.axes.plot(  x, y, label= alabel, linestyle = self.current_style[0], 
               marker = self.current_style[2],   color = self.current_style[1] )
        reset() to reset and reuse.  
              it will run forever but begin to repeate after a long cycle
    ?? add line weight and or other               
    """
    #   https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line
    # -----------------------------------------------
    def __init__(self ):

        # make elements relatively prime to give long cycle 
        self.lines       = [  '-', '--', ':' ]
        self.line_ix     = 0
        self.max_line    = len( self.lines  )

        # want dark distinct colors yellow and oarnge are light
        self.colors      = [ 'red', 'blue', 'cyan', 'green', 'black' ]   
        self.color_ix    = 0
        self.max_color   = len( self.colors  )

        self.markers     = [ 'o', 'x', '+', '*', 'h', 's' ]
        self.marker_ix   = 0
        self.max_marker  = len( self.markers  )

        self.reset( )
        
    # -----------------------------------------------
    def reset( self, ):
        """
        reset to initial stare, for reuse
        """
        self.line_ix     = 0
        self.color_ix    = 0
        self.marker_ix   = 0

    # -----------------------------------------------
    def get_line( self, ):
        """
        inside class use only,
        get next line sytle
        """
        ret       = self.lines[ self.line_ix ]
        self.line_ix  += 1
        if self.line_ix >= self.max_line:
            self.line_ix = 0
        return ret

    # -----------------------------------------------
    def get_color( self, ):
        """
        inside class use only,
        get next color sytle
        """
        ret       = self.colors[ self.color_ix ]
        self.color_ix  += 1
        if self.color_ix >= self.max_color:
            self.color_ix = 0
        return ret

    # -----------------------------------------------
    def get_marker( self, ):
        """
        inside class use only,
        get next marker sytle
        """
        ret       = self.markers[ self.marker_ix ]
        self.marker_ix  += 1
        if self.marker_ix >= self.max_marker:
            self.marker_ix = 0
        return ret

    # -----------------------------------------------
    def get_styles( self,  ):
        """
        get the next tuple: ( line, color, marker )
        """
        return ( self.get_line() , self.get_color(), self.get_marker() )

