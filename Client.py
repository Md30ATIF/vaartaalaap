import socket, threading, sys, time
from Crypto.Cipher import AES


destination = input("Specify Destination folder : ")
# destination = "C:/Users/User/Desktop"
try:
    test = open(destination + "/test.txt", 'w')
    test.write("Checking the destination folder! You may delete this file!")
    test.close()
except:
    print("Folder not found or access denied! Default location : Location of the Client_chatbox.py file")
    destination = '.'


s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
file_count = 0
transferred_file = open(destination + '/test.txt', 'ab')
key = s.recv(1024)
IV = str(s.recv(1024), 'utf-8')


def padding(message):
    return message + ' ' * (16 - len(message) % 16)


def pad_file(file_content):
    return file_content + b'0' * (16 - len(file_content) % 16)


def send():
    while True:
        message = input(">>")
        if message[:6] == "!file:":
            print("Sending file!")
            try:
                file_content = open(message[6:], 'rb').read()
                x = len(file_content)
                i, j = 0, min(1000, x)
                s.send(str.encode('0'))
                s.send(AES.new(key, AES.MODE_CBC, IV).encrypt(str.encode(padding("!file:"))))
                time.sleep(0.5)
                while j != x:
                    s.send(str.encode('1'))
                    # print(file_content[i:j][:20])
                    s.send(AES.new(key, AES.MODE_CBC, IV).encrypt(pad_file(file_content[i:j])))
                    time.sleep(0.1)
                    i, j = j, min(j + 1000, x)
                s.send(str.encode("1"))
                s.send(AES.new(key, AES.MODE_CBC, IV).encrypt(pad_file(file_content[i:j])))
            except:
                print(sys.exc_info()[1])
                print("File not found! Have you provided the full path?")
            continue
        s.send(str.encode('0'))
        s.send(AES.new(key, AES.MODE_CBC, IV).encrypt(str.encode(padding(message))))
threading.Thread(target=send).start()


while True:
    flag = int(str(s.recv(1024), "utf-8"))
    received = s.recv(1024)
    if flag == 0:
        port, message1 = str(AES.new(key, AES.MODE_CBC, IV).decrypt(received), "utf-8").split(' _:_ ')
    if flag == 1:
        transferred_file = open(destination + '/file' + str(file_count), 'ab')
        aes_string = AES.new(key, AES.MODE_CBC, IV).decrypt(received)
        # print(aes_string[:20])
        transferred_file.write(aes_string.rstrip(b'0'))
        transferred_file.close()
        continue
    if message1.strip() == "!file:":
        file_count += 1
        print(port, ':', "Receiving file{}!".format(file_count))
    else:
        print(port, ':', message1)
