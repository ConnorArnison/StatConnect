import socket
import psutil
import datetime
import time
import pickle


class HWData:
    def __init__(self, hostname, time, cpufreq, cpupercent, memory):
        self.hostname = hostname
        self.timestamp = time
        self.cpufreq = cpufreq
        self.cpupercent = cpupercent
        self.memory = memory


def measure_data():
    hostname = socket.gethostname()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cpufreq = psutil.cpu_freq()
    cpupercent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    return [hostname, st, cpufreq, cpupercent, memory]


def encode_data(hostname, time, cpufreq, cpupercent, memory):
    dataObject = HWData(hostname, time, cpufreq, cpupercent, memory)
    dataPickle = pickle.dumps(dataObject)
    return dataPickle


host = "192.168.1.14"
port = 2004

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))


while True:
    current_reading = measure_data()
    current_reading = encode_data(current_reading[0], current_reading[1], current_reading[2], current_reading[3], current_reading[4])
    tcpClient.sendall(current_reading)
    time.sleep(2)
