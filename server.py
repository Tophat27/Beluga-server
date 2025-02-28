import socket
import threading

HOST = '0.0.0.0'
PORT = 1234

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Dados de {addr}: {data.decode()}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()
        print(f"Conexão com {addr} encerrada")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor aguardando conexões em {PORT}...")
    
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
