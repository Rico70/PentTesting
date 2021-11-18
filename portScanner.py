import socket

s = socket.socket()

result = s.connect_ex(("rafaelrrodriguez.com",8090))

if(result == 0):
    print("Port is open")
else:
    print("Port is clsoed")