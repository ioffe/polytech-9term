import socket

def run():
   HOST, PORT = "localhost", 9999
   while True:
      sock = socket.socket()
      sock.connect((HOST, PORT))

      data = input('> ')
      sock.send(bytes(data + "\n","utf8"))
      received = sock.recv(1024)
      
      print("Sent:     %s" % data)
      print("Received: %s" % received)

      sock.close()


