# -*- coding: utf-8 -*-

"""



"""




import matplotlib.pyplot as plt     # plotting stuff
import moving_average
import sensor_simulator  as ss
import data_trigger      as dt
import line_style

"""
LoggingSim in simulate_logging.py
"""

# ========================== Begin Class ================================
class LoggingSim:
    """
    Show graph for logging with simulated noisy and processed data.
    """
    def __init__( self, ):

        self.version        = "2016 01 30.1"
        self.plot_title     = "plot_title"
        self.lines_ix       = 0   # lines in plot
        self.lineStyle      = line_style.LineStyle()

    # ------------------------------------------------
    def add_sensor_data(self, name, amplitude, noise_amp, delta_t, max_t, run_ave, trigger_value ):
        """
        Simulate a sensor and collect data with various parameters
            amplitude, noise_amp, delta_t, max_t, run_ave,
            trigger_value  sets the trigger level for time, data not saved untill trigger value is reached
        """
        # make a simulated sensor
        sensor  = ss.SensorSim( amplitude, noise_amp, delta_t = delta_t )

        data0       = []
        data1       = []
        x0          = 0.

        if trigger_value > 0:
            trigger = dt.DataTrigger( trigger_value )

        if run_ave > 0:
            averager = moving_average.MovingAverage( run_ave)

        while x0 < max_t:

             x0, x1 = sensor.get_next_sample()
             if run_ave > 0:
                 x1   = averager.nextVal( x1 )
             add_flag = True
             if trigger_value > 0:
                 add_flag = trigger.need_save( x0 )

             if add_flag:
                 data0.append( x0 )
                 data1.append( x1 )

        self.add_line( name, data0, data1 )

    # ------------------------------------------------
    def start_plot( self,  plot_title = "start_plot"  ):
        """
        start a plot process: initialize the graph
        no data yet, do only once for each graph
        return nothing but change object state
        """
        self.lineStyle.reset()
        self.plot_title =  plot_title

        self.lines_ix      = 0
        self.fig = plt.figure( figsize=(12, 12) )

        self.axes = self.fig.add_subplot(111)  # to have multiple lines in the plot

        self.axes.set_xlabel( 'Time' )
        self.axes.set_ylabel( 'Signal' )

        self.axes.set_title( self.plot_title )

        return

    # ------------------------------------------------
    def add_line( self, name, data0, data1 ):
        """
        add a line of data in variables x y to the graph
        label ( legend ) alabel
        return nothing
        """
        line_style  = self.lineStyle.get_styles()

        self.lines_ix      += 1
        self.axes.plot(  data0, data1, label = name,
                          linestyle = line_style[0], marker = line_style[2], color = line_style[1] )
        self.axes.legend( loc=2 ) #  set axes location: 4 is lower left  2 is upper left
        return

    # ------------------------------------------------
    def show_plot( self ):   # calling show seems to destroy the plot
        """
        show the plot
        should supress blank plot
        return nothing
        """
        if self.lines_ix <= 0:
            print( "show_plot() nothing to show" )
        else:
            plt.show( self.fig )
        return

    # ======================== begin experiments ==================
    # ------------------------------------------------
    def experiment_with_sample_rates( self ):
        print( """
        Experiment with Sample Rates
        Looking at different sample rates by changing delta T
        """ )
        self.start_plot( plot_title = "Experiment with Sample Rates - Part 1/3: Delta T = 1.0"  )

        self.add_sensor_data( name          = "dt = 1.",
                              amplitude     = 1.,
                              noise_amp     = .0,
                              delta_t       = 1.,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )
        self.show_plot( )

        # ------------------------------------------------
        self.start_plot( plot_title = "Experiment with Sample Rates - Part 2/3: Delta T = 0.1"  )
        self.add_sensor_data( name          = "dt = 1.",
                              amplitude     = 1.,
                              noise_amp     = .0,
                              delta_t       = 0.1,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )
        self.show_plot( )

        # ------------------------------------------------
        self.start_plot( plot_title = "Experiment with Sample Rates - Part 3/3: Delta T = 0.01"  )
        self.add_sensor_data( name          = "dt = 1.",
                              amplitude     = 1.,
                              noise_amp     = .0,
                              delta_t       = 0.01,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )
        self.show_plot( )

    # ------------------------------------------------
    def experiment_showing_noise( self ):
        print( """
        Experiment showing noise
        Looking at different amounts of noise by changing the noise amplitude.
        """ )
        self.start_plot( plot_title = "Experiment Showing Noise"  )

        self.add_sensor_data( name          = "noise = 0.0",
                              amplitude     = 1.,
                              noise_amp     = .0,
                              delta_t       = .1,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )

        self.add_sensor_data( name          = "noise = 0.1",
                              amplitude     = 1.,
                              noise_amp     = .1,
                              delta_t       = .1,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )

        self.add_sensor_data( name          = "noise = 1.0",
                              amplitude     = 1.,
                              noise_amp     = 1.,
                              delta_t       = .1,
                              max_t         = 10.,
                              run_ave       = 0,
                              trigger_value = 0 )
        self.show_plot( )

    # ------------------------------------------------
    def experiment_with_moving_average( self ):
        print( """
        Experiment with MovingAverage
        Looking at different MovingAverage by changing the length.
        All have the same noise.
        """ )
        # ------------------------------------------------
        self.start_plot( plot_title = "Experiment with MovingAverage - Part 1/2: No Moving Average" )
        self.add_sensor_data( name          = "ave len=0",
                               amplitude     = 1.,
                               noise_amp     = .1,
                               delta_t       = .1,
                               max_t         = 10.,
                               run_ave       = 0,
                               trigger_value = 0 )

        self.show_plot( )

        self.start_plot( plot_title = "Experiment with MovingAverage - Part 2/2: Len 8 and 32 Moving Average" )
        self.add_sensor_data( name          = "ave len=8",
                              amplitude     = 1.,
                              noise_amp     = .1,
                              delta_t       = .1,
                              max_t         = 10.,
                              run_ave       = 8,
                              trigger_value = 0 )

        self.add_sensor_data( name          = "ave len=32",
                              amplitude     = 1.,
                              noise_amp     = .1,
                              delta_t       = .1,
                              max_t         = 10.,
                              run_ave       = 32,
                              trigger_value = 0 )

        self.show_plot( )

    # ------------------------------------------------
    def experiment_with_moving_average_and_sample_rate( self ):
        print( """
        Experiment with Moving Average and Sample Rate,
              dt,
              run average being varied
        """ )
        # ------------------------------------------------
        self.start_plot( plot_title = "Experiment with Moving Average and Sample Rate"  )

        self.add_sensor_data( name          = "dt=.1 ra=0 trig=0",
                               amplitude     = 1.,
                               noise_amp     = .1,
                               delta_t       = .1,
                               max_t         = 10.,
                               run_ave       = 0,
                               trigger_value = 0 )

        self.add_sensor_data( name          = "dt=.1 ra=10 trig=0",
                               amplitude     = 1.,
                               noise_amp     = .1,
                               delta_t       = .1,
                               max_t         = 10.,
                               run_ave       = 10,
                               trigger_value = 0 )

        self.add_sensor_data( name          = "dt=.01 ra=100 trig=0",
                              amplitude     = 1.,
                              noise_amp     = .1,
                              delta_t       = .01,
                              max_t         = 10.,
                              run_ave       = 100,
                              trigger_value = 0 )
        self.show_plot( )

    # ------------------------------------------------
    def experiment_with_trigger( self ):
        print( """
        Experiment with Triggering,
              dt,
              run average
              and trigger all being varied
        """ )
        # ------------------------------------------------
        self.start_plot( plot_title = "An Experiment with Trigger 1/1 - Triggering On"  )

        self.add_sensor_data( name          = "dt=.1 ra=10, trig =0",
                               amplitude     = 1.,
                               noise_amp     = .1,
                               delta_t       = .1,
                               max_t         = 10.,
                               run_ave       = 10,
                               trigger_value = 0 )

        self.add_sensor_data( name          = "dt=.01 ra=100, trig =.1",
                              amplitude     = 1.,
                              noise_amp     = .1,
                              delta_t       = .01,
                              max_t         = 10.,
                              run_ave       = 100,
                              trigger_value = .1 )
        self.show_plot( )

    # ------------------------------------------------
    def experiment_with_trigger_louder_noise( self ):
        print( """
        Louder noise than prior experiment
        """ )
        self.start_plot( plot_title = "An Experiment with Trigger - Louder Noise"  )

        self.add_sensor_data( name          = "...dt=.1 ra=10",
                               amplitude     = 1.,
                               noise_amp     = .5,
                               delta_t       = .1,
                               max_t         = 10.,
                               run_ave       = 10,
                               trigger_value = 0 )

        self.add_sensor_data( name          = "..dt=.01 ra=100 tv =.1",
                              amplitude     = 1.,
                              noise_amp     = .5,
                              delta_t       = .01,
                              max_t         = 10.,
                              run_ave       = 100,
                              trigger_value = .1 )
        self.show_plot( )

# ------------------------------------------------
if __name__ == '__main__':
        """
        run the app
        comment, uncomment the experiments, or create your own.
        """
        print( "=========Run LoggingSim===============" )
        sim_logging    = LoggingSim(  )

        # comment uncomment to run experiments
        sim_logging.experiment_with_sample_rates()
        #sim_logging.experiment_showing_noise()
        #sim_logging.experiment_with_moving_average()
        #sim_logging.experiment_with_moving_average_and_sample_rate( )
        #sim_logging.experiment_with_trigger()
        #sim_logging.experiment_with_trigger_louder_noise()

        print( "---------End LoggingSim----------------" )


# ==================== eof =============================

