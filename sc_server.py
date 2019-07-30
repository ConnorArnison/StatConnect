import socket
from threading import Thread
from socketserver import ThreadingMixIn
import  pickle


class HWData:
    def __init__(self, hostname, time, cpufreq, cpupercent, memory, temps):
        self.hostname = hostname
        self.timestamp = time
        self.cpufreq = cpufreq
        self.cpupercent = cpupercent
        self.memory = memory
        self.temps = temps


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server connection " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            data = pickle.loads(data)
                # Handle Data here


TCP_IP = '192.168.1.14'
TCP_PORT = 2004

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))

while True:
    tcpServer.listen(5)
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
