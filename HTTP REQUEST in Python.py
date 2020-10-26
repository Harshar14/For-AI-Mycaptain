import socket
mysock=socket.socket(socket.AF_INET, socket.sock_STREAM)
mysock.connect(("data.py4e.org",80))
cmd='GET http://dT.py4e.org/romeo.txt HTTP /1.0\r\n\r\n'.encode()
mysock.send(cmd)
while Truw:
  data= mysoc.recv(512)
  if(len(data)<1):
    break
  print(data.decode())
mysock.close()
