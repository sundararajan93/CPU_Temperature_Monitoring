import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-darkgrid')

def animate(i):
    data = pd.read_csv('sensor_data.csv')
    x = data['SN']
    y = data['core0']
    y1 = data['core1']

    critical = 54
    normal = 45

    plt.cla()
    plt.plot(x, y, label="Core 0")
    plt.plot(x, y1, label="Core 1")
    plt.axhline(critical, color='red', linestyle='--', linewidth=1, label='Critical')
    plt.axhline(normal, color='green', linestyle='--', linewidth=1, label='Normal')
    plt.legend(loc='upper left')
    plt.title("CPU Temperature")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature in Celcius")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

