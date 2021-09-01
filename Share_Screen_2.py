from vidstream import StreamingServer
from vidstream import ScreenShareClient
from tkinter import *
import socket

root = Tk()
root.geometry("1680x680")



label = Label(root, text="Ip to connect: ")
label.pack()

e2 = Entry()
e2.pack()

def listen():
    ip_to_listen = socket.gethostname()
    server = StreamingServer(ip_to_listen, 9999)
    server.start_server()


button = Button(text="connect",command=listen)
button.pack()



def screen():
    ip_to_connect = e2.get()
    client1 = ScreenShareClient(ip_to_connect, 9999)
    client1.start_stream()

label = Label(root, text="\n")
label.pack()

button = Button(text="Start share screen",command=screen)
button.pack()


root.mainloop()