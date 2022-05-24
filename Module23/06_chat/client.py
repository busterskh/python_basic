import socket

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('Твой iP: ', ip)
server_host = input('Введи iP-адрес получателя: ')
name = input('Введи имя: ')


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' подключен...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    user_action = int(input('\n1. Посмотреть текущий текст чата.\n'
                            '2. Отправить сообщение.\n'))
    if user_action == 2:
        message = input("Me : ")
        with open('chat_history.txt', 'a') as history:
            history.write(name + ':')
            history.write('\t' + message + '\n')
        socket_server.send(message.encode())
    elif user_action == 1:
        with open('chat_history.txt', 'r') as history:
            for line in history:
                print(line[:-1])
