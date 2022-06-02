import socket

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("Успешная привязка!")
print("Это твой iP-адрес, используй его для подключения: ", s_ip)

name = input('Введи имя: ')

new_socket.listen(5)


conn, add = new_socket.accept()

print('Соединение установлено. Подключение от : ', add[0])

client = (conn.recv(1024)).decode()
print(client + ' подключился.')

conn.send(name.encode())

while True:
    user_action = int(input('\n1. Посмотреть текущий текст чата.\n'
                            '2. Отправить сообщение.\n'))
    if user_action == 2:
        message = input('Me : ')
        conn.send(message.encode())
        with open('chat_history.txt', 'a') as history:
            history.write(name + ':')
            history.write('\t' + message + '\n')
        message = conn.recv(1024)
        message = message.decode()
        print(client, ':', message)
    elif user_action == 1:
        with open('chat_history.txt', 'r') as history:
            for line in history:
                print(line[:-1])

