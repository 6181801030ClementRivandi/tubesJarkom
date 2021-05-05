import socket, threading
from tkinter import *

#window#

window = Tk()

window.title("tic tac toe by 6181801030 and 6181801060")
window.geometry("400x400")

#grid#

#row 1

leftTopBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 11)
leftTopBtn.grid(column = 1, row = 1)
centerTopBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 21)
centerTopBtn.grid(column = 2, row = 1)
rightTopBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 31)
rightTopBtn.grid(column = 3, row = 1)

#row 2
leftCenterBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 12)
leftCenterBtn.grid(column = 1, row = 2)
centerCenterBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 22)
centerCenterBtn.grid(column = 2, row = 2)
rightCenterBtn = Button(window, text = " ", bg = "white", width = 6, height = 3,  command = 32)
rightCenterBtn.grid(column = 3, row = 2)

#row 3
leftBottomBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 13)
leftBottomBtn.grid(column = 1, row = 3)
centerBottomBtn = Button(window, text = " ", bg = "white", width = 6, height = 3, command = 23)
centerBottomBtn.grid(column = 2, row = 3)
rightBottomBtn = Button(window, text = " ", bg = "white", width = 6, height = 3,  command = 33)
rightBottomBtn.grid(column = 3, row = 3)

window.mainloop()

playerAktif = True

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print ("from client", msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

