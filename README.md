This repository contains a CLI based chatbox with end to end AES encription for the Server and Client code. It allows to connect and interact multiple users among themselves by connecting them to the Server. The code has been developed to function over the localhost only. But the same can be extended to function over the internet.

# LIBRARIES REQUIRED :
- sockets( pip install socket.py )
- pycrypto( pip install pycrypto==2.0.1 )

# SALIENT FEATURES
## Multi user interface :
A large no. of users can connect to the server provided they have the Client code and interact amongst themselves. There are NO restrictions on the no. of users who can connect at the same time in the program(Although being a multithreaded program, with the no. of threads increasing with the no. of new users, the computer's memory on which the server is running might be a restricting factor)
## Supported in all OS :
The program can be perfectly run in all operating systems as long as Python 3 is installed. NO extra libraries are required.
## Flexibility :
Users can enter and leave the program whenever they want as per there convenience, this won't affect the functioning of the program. Although the users who entered late won’t have any access to the previous messages shared among the users.
## Encrypted Messages :
The messages and files shared across are encrypted using AES with a randomly generated key and IV (Initialisation vector). Hence in case of a “Man in the middle” attack, no data loss will occur. The encryption procedure is very simple. A random key and IV is generated as the server starts running. These values are sent to a client as soon as the connection is established. AES being a symmetric cipher uses the same key for encryption and decryption. When a user sends a message or a file, it gets transferred to the server which broadcasts the message or file to all the other clients. The program at the client side, decrypts the message using the key and IV received in the beginning.
## File Transfer :
Not only messages but also files can be transferred from one user to another. Also there's no restriction to the file size (But larger the file, larger will be the time taken for the transfer!).
## Privacy :
On running the client file, the file asks for a destination folder to store the incoming files. The program only needs access to that folder. The rest of the files and folders remain inaccessible to the program.

# DISADVANTAGES :
## Restriction on message lenght :
It can be seen in the program that the buffer size is 1024. Therefore there will be a limitation to the size of the messages (i.e if a large message is sent, the whole message won't reach the other users). However that problem won’t occur upto a stretch of at least 1000 characters, therefore you’re safe as long as you’re not planning on sending a really long essay or something! Even if you are, just break the message. That’s it!
