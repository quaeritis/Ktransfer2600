# Ktransfer2600
A high-level user interface for Keithley 2600 series instruments which allows the user to configure, record and save voltage sweeps such as transfer and output measurements. Since there typically is no need to provide a live stream of readings from the Keithley, the data from an IV-curve is buffered locally on the instrument and only transferred to CustomXepr after completion of a measurement.

## System requirements
*Required*:

- Linux or macOS
- Python 3.x

## Acknowledgements
Config file modules are based on the implementation from [Spyder](https://github.com/spyder-ide).
