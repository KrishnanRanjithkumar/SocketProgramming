import socket
import threading
import time
from datetime import datetime
import traceback
import ssl

class ServerSocket:

    def __init__(self, server=None):
        if server is None:
            
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.context.load_cert_chain('C:/Users/Ranjith/Desktop/New folder/server.pem','C:/Users/Ranjith/Desktop/New folder/server.key')
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(("127.0.0.1",3443))
            self.server.listen(100)
            self.sslserver=self.context.wrap_socket(self.server, server_side=True)
            print(f'server started listening on port 3443')
        
        else:
            self.sslserver = server
        
        
        self.clients = []

    
      
    def broadcast(self,client):
        while True:
            try:
                time.sleep(10)
                time_message = datetime.now()
                client.send(str(time_message).encode('ascii'))
            except:
                print(traceback.print_exc())
                self.clients.remove(client)
                client.close()
                break


    def client_handler(self,client,address):
        while True:
            try:
                message = client.recv(1024)
                reversed_message = str(message.decode('ascii'))[::-1]
                client.send(str(reversed_message).encode('ascii'))
            except:
                print(traceback.print_exc())
                self.clients.remove(client)
                client.close()
                break

    def start(self):
        while True:
            try:
                 
                client, address = self.sslserver.accept()
                print(f'New client connected from {str(address)}')
                self.clients.append(client)
                client_thread = threading.Thread(target=self.client_handler, args=(client,address,))
                broadcast_date = threading.Thread(target=self.broadcast,args=(client,))
                client_thread.start()
                broadcast_date.start()
            except:
                print(traceback.print_exc())


if __name__ == "__main__":
    server = ServerSocket()
    server.start()

