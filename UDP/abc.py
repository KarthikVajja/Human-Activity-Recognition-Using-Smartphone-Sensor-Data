import socket, traceback, string
from sys import stderr
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
while 1:
    try:
        message, address = s.recvfrom(8192)
        print(message.decode())
        print("\n\n\n\n\n")
        message=message.decode()
        data = message.split( "," )
        t = data[0]
        sensorID = int(data[1])
        if sensorID==3:     
            ax, ay, az = data[2], data[3], data[4]
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
while 1:
    data,addr=s.recvfrom(8192)
    
    
