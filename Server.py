# -*- coding: utf-8 -*-
import threading, socket, random, os
from Crypto.Cipher import AES
_receive_ = []
clients = []
s = socket.socket()
s.bind(('', 12345))
print("Bound")
s.listen()
message_count = 0
message = ''
count = 0
key = random.randint(0, 256)
key1 = os.urandom(16)
mode = AES.MODE_CBC
IV = ''
for _ in range(16):
    IV += chr(random.randint(32, 126))


def padding(message):
    return message + ' ' * (16 - len(message) % 16)


def receive():
    global t1
    global message
    global message_count
    c, addr = s.accept()
    c.send(key1)
    c.send(str.encode(IV))
    clients.append(c)
    _receive_.append(t1)
    print("Received connection!")
    t1 = threading.Thread(target=receive)
    t1.start()
    while True:
        flag = str(c.recv(1024), "utf-8")
        for i in clients:
            if i != c:
                i.send(str.encode(flag))
        shit = c.recv(1024)
        message_count += 1
        
        if flag == '0':
            message = str(AES.new(key1, AES.MODE_CBC, IV).decrypt(shit), "utf-8")
            for i in range(len(clients)):
                if clients[i] != c:
                    qwerty = str.encode(padding(str(addr[1]) + ' _:_ ' + message.strip()))
                    clients[i].send(AES.new(key1, AES.MODE_CBC, IV).encrypt(qwerty))
        
        if flag == '1':
            for i in clients:
                if i != c:
                    i.send(shit)

t1 = threading.Thread(target=receive)

t1.start()
while True:
    if count != message_count:
        count += 1