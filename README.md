# CPU_Temperature_Monitoring
This utility is used to monitor the live temperature of cpu cores in linux machines. The tool is designed with Python library Matplotlib
The tool which I developed supports only linux machines for now. I have a plan to port it to cross platform in the near future

# Pre-requisites
* Python 3.x
* Matplotlib
* Sensors

# Installing Pre-requisites

```
sudo apt-get install python3.6
pip3 install matplotlib
sudo apt-get install sensors
```

# Running the tool

```git clone https://github.com/sundararajan93/CPU_Temperature_Monitoring
cd CPU_Temperature_Monitoring```

open the terminal and run '11_Sensor_value.py'(This is the demon which creates a CSV file to the directory from where our graph pulls data)
<br/>```python3 11_Sensor_value.py```

Now lets run the main Dashboard to view live CPU temperatures from another terminal
<br/>
```python3 12_Realtimedata_CSV.py'```

NOTE: Do not close the demon (11_Sensor_value.py)
This will stop the data feed to CSV file(sensor_data.csv) created in the directory
