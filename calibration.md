# Calibration

We validated and characterized the instrument using water ice-point and boiling-point calibrations with a single sensor.

An ice-point calibration was performed with an ice-water mixture in a 500 ml beaker.
During the ice-point calibration 100 data points were taken at 5 second intervals with a shielded thermocouple.
The thermocouple was placed near the top of the container where both ice and water were present.
The observed mean over the 100 samples was from 2.52 degrees celsius and the standard deviation was 0.072 degrees Celsius.

A boiling point calibration was performed with 500 ml of boiling water on a laboratory hot plate.
During the boiling-point calibration, 100 data points were taken at 1 second intervals with a shielded thermocouple.
The mean reading was 98.7 degrees with a standard deviation of 0.15 degrees Celsius.

These means are consistent with a typical thermocouple accuracy of 2.2 C and the deviations are consistent with the MAX 31855 amplifier resolution of 0.25 C.
For users wanting higher control over calibration, the cold-junction compensation code can be accessed in the MAX31855 CircuitPython library.
