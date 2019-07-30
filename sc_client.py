import socket
import psutil
import datetime
import time
import pickle


class HWData:
    def __init__(self, hostname, time, cpufreq, cpupercent, memory, temps):
        self.hostname = hostname
        self.timestamp = time
        self.cpufreq = cpufreq
        self.cpupercent = cpupercent
        self.memory = memory
        self.temps = temps


def MeasureData():
    hostname = socket.gethostname()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cpufreq = psutil.cpu_freq()
    cpupercent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    temps = psutil.sensors_temperatures()
    return [hostname, st, cpufreq, cpupercent, memory, temps]


def EncodeData(hostname, time, cpufreq, cpupercent, memory, temps):
    dataObject = HWData(hostname, time, cpufreq, cpupercent, memory, temps)
    dataPickle = pickle.dumps(dataObject)
    return dataPickle


host = socket.gethostname()
port = 2004

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))


while True:
    current_reading = MeasureData()
    current_reading = EncodeData(current_reading[0], current_reading[1], current_reading[2], current_reading[3], current_reading[4], current_reading[5])
    tcpClient.sendall(current_reading)
    time.sleep(2)
