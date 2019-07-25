import socket
import psutil
import datetime
import time
import pickle


class HWData:
    def __init__(self, ip, time, cpu, memory):
        self.ip = ip
        self.timestamp = time
        self.cpu = cpu
        self.memory = memory


def MeasureData():
    ip = socket.gethostname()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()[2]
    return [ip, st, cpu, memory]


def EncodeData(ip, time, cpu, memory):
    dataObject = HWData(ip, time, cpu, memory)
    dataPickle = pickle.dumps(dataObject)
    return dataPickle


host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2048

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))



while True:
    current_reading = MeasureData()
    current_reading = EncodeData(current_reading[0], current_reading[1], current_reading[2], current_reading[3])
    tcpClient.send(current_reading)
    time.sleep(2)

tcpClient.close()