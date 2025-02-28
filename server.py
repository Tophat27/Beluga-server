import socket

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 1234        # Porta usada no código da XIAO

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor TCP ativo em {PORT}. Aguardando conexões...")
    
    while True:
        conn, addr = s.accept()
        print(f"Conectado por {addr}")
        
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Dados recebidos:", data.decode())
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()
            print("Conexão encerrada.")
