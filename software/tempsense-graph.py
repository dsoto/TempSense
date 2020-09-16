import time
import board
import busio
import digitalio
import adafruit_max31855

import datetime

from bokeh.plotting import figure, ColumnDataSource
from bokeh.io import curdoc

# initalizations

log_interval_ms = 1E3

# maybe don't use arrays here either if not necessary
# continue plotting to screen

def config_sensors():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = [digitalio.DigitalInOut(board.D4),
          digitalio.DigitalInOut(board.D5),
          digitalio.DigitalInOut(board.D6),
          digitalio.DigitalInOut(board.D7)]
    return [adafruit_max31855.MAX31855(spi, cs[0]),
            adafruit_max31855.MAX31855(spi, cs[1]),
            adafruit_max31855.MAX31855(spi, cs[2]),
            adafruit_max31855.MAX31855(spi, cs[3])]

def read_temps(sensors):
    return [sensors[0].temperature,
            sensors[1].temperature,
            sensors[2].temperature,
            sensors[3].temperature]

def write_temps(log_file, temps, sample_time):
    with open(log_file, 'a') as f:
        f.write(sample_time.strftime('%Y-%m-%dT%H:%M:%S'))
        #f.write(',')
        for temp in temps:
            f.write(',{}'.format(temp))
        f.write('\n')

sensors = config_sensors()


# this is where we define our graphs and connect them to our data
def make_document(doc):

    # this is where we read our data and place it in the array for the graph data
    # this function is called by doc.add_periodic_callback
    def update():

        # read temperatures and place in column data store
        # TODO: make this more verbose?
        temps = read_temps(sensors)
        sample_time = datetime.datetime.now()
        write_temps(log_file, temps, sample_time)

        # adds a measurement to the graphing temperatures
        # this adds a row to the table
        # .stream adds a row of data to this table
        # TODO: change this name to graph_data
        temp_source.stream({'time': [sample_time],
                            'temp0': [temps[0]],
                            'temp1': [temps[1]],
                            'temp2': [temps[2]],
                            'temp3': [temps[3]]})

    # special place to hold temperatures for graphing
    # we can think of this as a table with columns
    temp_source = ColumnDataSource({'time': [],
                                    'temp0': [],
                                    'temp1': [],
                                    'temp2': [],
                                    'temp3': []})

    # TODO: make this plot set up stuff flow if possible
    # TODO: make document, make plot, set up update, then add lines and shapes

    # tells the computer to update the graph at a regular time interval
    doc.add_periodic_callback(update, log_interval_ms)

    # creates a plot
    temp_fig = figure(title = '', x_axis_type='datetime')
    temp_fig.xaxis.axis_label = 'Time'
    temp_fig.yaxis.axis_label = 'Temperature (C)'

    # create lines for each temperature measurement
    # do we want lines at all?  too much complexity?
    # each line uses data from our temperature table above
    temp_fig.line(source=temp_source, x='time', y='temp0', legend='1 (CS5)', line_width=1, color='blue')
    temp_fig.line(source=temp_source, x='time', y='temp1', legend='2 (CS6)', line_width=1, color='green')
    temp_fig.line(source=temp_source, x='time', y='temp2', legend='3 (CS7)', line_width=1, color='red')
    temp_fig.line(source=temp_source, x='time', y='temp3', legend='4 (CS8)', line_width=1, color='black')

    # create shapes and colors and sizes for each temperature measurement
    temp_fig.circle(source=temp_source, x='time', y='temp0', size=4, color='blue')
    temp_fig.circle(source=temp_source, x='time', y='temp1', size=4, color='green')
    temp_fig.circle(source=temp_source, x='time', y='temp2', size=4, color='red')
    temp_fig.circle(source=temp_source, x='time', y='temp3', size=4, color='black')

    # set up the figure and the plot
    plots = temp_fig
    doc.add_root(plots)
    doc.title = "Temperature Plotting"

print('starting')

# TODO: how do you make this cleaner for first-time readers
log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '-log.csv'
with open(log_file, 'w') as f:
    f.write('time,temp_1_C,temp_2_C,temp_3_C,temp_4_C\n')

print('logging to file {}'.format(log_file))

# this is a mysterious command that creates the webpage and the plot within it
make_document(curdoc())
