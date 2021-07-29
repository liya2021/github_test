import  socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))

s.listen(5)

c,addr = s.accept()

c.send('huanyinghuijia')

c.close()