import time
import board
import busio
import digitalio
import adafruit_max31855

import datetime

from bokeh.plotting import figure, ColumnDataSource
from bokeh.io import curdoc

# initalizations

log_interval_ms = 5E3

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

def make_document(doc):

    def update():
        # read and place in column data store
        temps = read_temps(sensors)
        sample_time = datetime.datetime.now()
        write_temps(log_file, temps, sample_time)
        temp_source.stream({'time': [sample_time],
                            'temp0': [temps[0]],
                            'temp1': [temps[1]],
                            'temp2': [temps[2]],
                            'temp3': [temps[3]]})

    temp_source = ColumnDataSource({'time': [],
                                    'temp0': [],
                                    'temp1': [],
                                    'temp2': [],
                                    'temp3': []})

    doc.add_periodic_callback(update, log_interval_ms)

    temp_fig = figure(title='TEMP', x_axis_type='datetime')

    temp_fig.line(source=temp_source, x='time', y='temp0',
                    legend='CS 5', color='blue')
    temp_fig.line(source=temp_source, x='time', y='temp1',
                    legend='CS 6', color='green')
    temp_fig.line(source=temp_source, x='time', y='temp2',
                    legend='CS 7', color='red')
    temp_fig.line(source=temp_source, x='time', y='temp3',
                    legend='CS 8', color='black')

    temp_fig.circle(source=temp_source, x='time', y='temp0', color='blue')
    temp_fig.circle(source=temp_source, x='time', y='temp1', color='green')
    temp_fig.circle(source=temp_source, x='time', y='temp2', color='red')
    temp_fig.circle(source=temp_source, x='time', y='temp3', color='black')
    plots = temp_fig
    doc.add_root(plots)
    doc.title = "Temperature Plotting"

print('starting')

log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '-log.csv'
with open(log_file, 'w') as f:
    f.write('time,temp_1_C,temp_2_C,temp_3_C,temp_4_C\n')

print('logging to file {}'.format(log_file))

make_document(curdoc())
