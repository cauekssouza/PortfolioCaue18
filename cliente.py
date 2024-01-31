import socket
import threading

def recebeDados(conn):
    try:
        while True:
            mensagem = conn.recv(1024).decode()
            print(mensagem)
    except socket.error as e:
        print(f'Erro no recebimento de mensagens do servidor: {e}')
    finally:
        conn.close()

# Substitua "26.208.0.68" pelo endereço IP real do servidor
HOST = "26.253.16.0"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

try:
    nome = input("Informe o seu nome: ")
    sock.sendall(str.encode(nome))
    print("----- CHAT INICIADO -----")

    threadRecebeDados = threading.Thread(target=recebeDados, args=[sock])
    threadRecebeDados.start()

    while True:
        mensagem = input(f'{nome} >> ')
        sock.sendall(str.encode(mensagem))
        if mensagem.lower() == 'sair':
            break

except socket.error as e:
    print(f'Erro ao se conectar ao servidor: {e}')

finally:
    sock.close()
    print("A conexão com o servidor foi finalizada")
