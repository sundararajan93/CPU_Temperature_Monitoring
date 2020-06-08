import os
import time
import csv


with open('sensor_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "core0", "core1"])


for i in range(10000):
    with open('sensor_data.csv', 'a') as file:
        writer = csv.writer(file)
        core_0 = os.popen("sensors -u | awk 'NR==4 {print $2}'").read()
        core_1 = os.popen("sensors -u | awk 'NR==9 {print $2}'").read()
        time.sleep(1)
        print(i, core_0.strip(), core_1.strip())
        writer.writerow([i, core_0.strip(), core_1.strip()])



