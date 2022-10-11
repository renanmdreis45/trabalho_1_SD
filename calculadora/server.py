 #importando bibliotecas
import socket
import operator

#definido açoes para cada operador 
operadores = { 
            "+": operator.add, 
            "-": operator.sub, 
            '*' : operator.mul,
            '/' : operator.truediv,  
            }
#ip e porta
IP = "127.0.0.1"
PORT = 12000
#tipo de soquete udp 
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

print('Servidor ouvindo em {}'.format(socket.getsockname()))

while True:
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Recebido do cliente {} : {}'.format(address, messageString))

    messageString = messageString.split(", ")
    a = messageString[0]
    b = messageString[1]
    operator = messageString[2]

    if a == 'X' or b == 'X' or operator == 'X':
        break

    result = operadores[operator](int(a), int(b))


    socket.sendto(str(result).encode(), address)


print('Conexeção Encerrada')
socket.close() 