import socket

IP = "127.0.0.1"
PORT = 12000

print('Cauculadora UDP, Seja bem vindo! \n - Pressione X caso deseje sair\n - insirra o valor de A e B e o operador para realizar a operação')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Digite o valor de A')
    a = input()

    print('Digite o valor de B')
    b = input()

    print('Operador aritimetico')
    operador = input()



    message = a + ', ' + b + ', ' + operador
    print('Mensagem sendo enviada para o servidor: ' + message + "\n")

    socket.sendto(message.encode('utf-8'), (IP, PORT))
    if a == 'X' or b == 'X' or operador == 'X':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Resultado recebido do servidor %s : %s ' % (address, text) + "\n")

print('Conexão encerrada')
socket.close() 