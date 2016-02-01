# Sensor-Polling

### Warning -- Incomplete Readme

### Overview
Sensor polling is one of two components in this anomaly detection tool:

1. Sensor polling and data collection, via automated sensors within the smart home
2. An [anomaly detection algorithm] (https://github.com/Merit-Research/BLR-Detection-Alg) 

Sensor-Polling is responsible for retrieving data from [Z-Wave] (http://www.z-wave.com/what_is_z-wave) 
compliant smart home sensors and supplying it to the [detection algorithm] (https://github.com/Merit-Research/BLR-Detection-Alg)
in the correct format. 

### Configuration and Usage
#### Required Python Modules
+ [matplotlib](http://matplotlib.org/users/installing.html)
+ [numpy](http://www.scipy.org/scipylib/download.html)

#### Configuration
Before using Sensor-Polling, the user must rename [sample-config.txt] (https://github.com/Merit-Research/Sensor-Polling/blob/master/sample-config.txt) to "config.txt" and edit "config.txt". Alternatively, the user may copy the [sample-config.txt] (https://github.com/Merit-Research/Sensor-Polling/blob/master/sample-config.txt) to another file named "config.txt" and edit "config.txt". 

i.e.
```
mv sample-config.txt config.txt
```
or
```
cp sample-config.txt config.txt
```

##### config.txt
config.txt contains all pertinent information needed by the Sensor-Polling software in order to contact the Z-Wave server and sensors. This information must be changed to contain the users' configurations after creation.

##### sensors.json
sensors.json contains all pertinent information needed by the Sensor-Polling software in order to contact the Z-Wave sensors as well as information regarding the use of the program and it's parameters. The fields contained within sensors.json are discussed below: 
+ generate
    + generate specifies what operations the program will perform. Options are 'data', which will log data to a text file, 'graph' which will graph the data using matplotlib and, 'both', which will both graph the data and record it to a text file.
+ delay
    + Delay is the interval (in milliseconds) that the program will obtain sensor data
+ datadirectory 
    + datadirectory is the absolute path to the directory where the user would like to store the data text files
+ time
    + refreshurl
        + a URL used to refresh the time device
    + dataurl
        + a URL used to obtain updateTime data from a sensor 
+ sensors
    + graphnumber
        + graphnumber is a number indicating which plot to graph the data on (only applies if 'generate' is set to 'graph' or 'both')
    + legend
        + legend is the name that will be used for the legend on the graph (only applies if 'generate' is set to 'graph' or 'both')
    + linecolor
        + linecolor is a hexadecimal color that will be used for the plotted line (only applies if 'generate' is set to 'graph' or 'both')
    + refreshurl
        + a url used to refresh the device
    + dataurl
        + a url used to obtain the device data
    + interpret
        + interpret defines what data type the data should be interpreted as, options are 'bool' and 'double'
    + graphto
        + graphto behaves different for different data types. For data interpreted as 'bool', graphto acts as the value that will be graphed when the data returns True. Alternatively, for data interpreted as 'double', graphto acts as the maximum value that data will be 

### License
