'''
Copyright 2019 Daniel Soto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import board                  # this library defines the metal pins on the board
import busio                  # this library allows us to speak SPI
import digitalio              # this library lets us turn metal pins on and off
import adafruit_max31855      # this library know how to talk to the temperature board
import datetime               # this library knows the clock and the calendar

# library to make plot and data source
from bokeh.plotting import figure, ColumnDataSource
# library to place graph on webpage
from bokeh.io import curdoc

# This script uses arrays, dictionaries, date and time formatting codes (strftime) and callback functions.
# Search for these python concepts online to understand any unfamiliar syntax.

# this function returns an array of sensor objects that can be handled as a unit
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

# this function reads the temperature of each of thermocouples
def read_temps(sensors):
    return [sensors[0].temperature,
            sensors[1].temperature,
            sensors[2].temperature,
            sensors[3].temperature]

# this function writes each of the temperatures to a line in a logging file
def write_temps(log_file, temps, sample_time):
    with open(log_file, 'a') as f:
        f.write(sample_time.strftime('%Y-%m-%dT%H:%M:%S'))
        for temp in temps:
            f.write(',{}'.format(temp))
        f.write('\n')


# this is where we define our graphs and connect them to our data
def make_document(webpage):

    # this is where we read our data and place it in the array for the graph data
    # this function is called by doc.add_periodic_callback
    def update():

        # read temperatures and place in column data store
        temps = read_temps(sensors)
        sample_time = datetime.datetime.now()
        write_temps(log_file, temps, sample_time)

        # adds a measurement to the graphing temperatures
        # this adds a row to the table
        # .stream adds a row of data to this table
        graph_data.stream({'time': [sample_time],
                            'temp0': [temps[0]],
                            'temp1': [temps[1]],
                            'temp2': [temps[2]],
                            'temp3': [temps[3]]})

    # special place to hold temperatures for graphing
    # we can think of this as a table with columns
    graph_data = ColumnDataSource({'time': [],
                                   'temp0': [],
                                   'temp1': [],
                                   'temp2': [],
                                   'temp3': []})


    # creates a plot figure, labels axes, and sets x-axis as time
    graph = figure(title='TempSense v0.2', x_axis_type='datetime')
    graph.xaxis.axis_label = 'Time'
    graph.yaxis.axis_label = 'Temperature (C)'

    # create lines for each temperature measurement
    # each line uses data from 'graph_data' above
    # the x and y labels match the labels in 'graph_data'
    graph.line(source=graph_data, x='time', y='temp0', legend_label='T1', line_width=1, color='blue')
    graph.line(source=graph_data, x='time', y='temp1', legend_label='T2', line_width=1, color='green')
    graph.line(source=graph_data, x='time', y='temp2', legend_label='T3', line_width=1, color='red')
    graph.line(source=graph_data, x='time', y='temp3', legend_label='T4', line_width=1, color='black')

    # create shapes and colors and sizes for each temperature measurement
    graph.circle(source=graph_data, x='time', y='temp0', size=4, color='blue')
    graph.circle(source=graph_data, x='time', y='temp1', size=4, color='green')
    graph.circle(source=graph_data, x='time', y='temp2', size=4, color='red')
    graph.circle(source=graph_data, x='time', y='temp3', size=4, color='black')

    # set the legend location on the graph
    graph.legend.location = 'top_left'

    # add the graph to a web page and call update periodically
    webpage.add_root(graph)
    webpage.title = "TempSense v0.2"
    # tells the computer to update the graph by calling the "update" function at a regular time interval
    webpage.add_periodic_callback(update, log_interval_ms)

# below this line are the commands executed by the script
# (above this we defined the functions, but did not run them)

# create an array of temperature sensor objects
sensors = config_sensors()
# set the time between temperature readings in milliseconds
log_interval_ms = 5000

# creates a filename with the current date and time and writes the header line to the file
log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '-log.csv'
with open(log_file, 'w') as f:
    f.write('time,temp_1_C,temp_2_C,temp_3_C,temp_4_C\n')

# send messages to the output console
print('Starting temperature instrument')
print('logging to file {}'.format(log_file))

# this command creates the webpage and the plot within it by running the 'make_document' function above
# note curdoc() is called webpage in 'make_document'
make_document(curdoc())
