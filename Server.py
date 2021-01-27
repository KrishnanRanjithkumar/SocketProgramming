import socket
import threading
import time
from datetime import date
import traceback
import ssl
import os

class ServerSocket:

    def __init__(self, server=None):
        """
        Starts the localhost server on 3443
        """
        if server is None:
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.cwd=os.path.dirname(os.path.realpath(__file__))
            self.context.load_cert_chain(self.cwd+'/server.pem',self.cwd+'/server.key')
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(("127.0.0.1",3443))
            self.server.listen(100)
            self.sslserver=self.context.wrap_socket(self.server, server_side=True)
            print(f'server started listening on port 3443')
        
        else:
            self.sslserver = server
        
        
        self.clients = []

    
      
    def broadcast(self,client):
        """
        Broadcast current date to the connected clients 
        every 10 seconds
        
        """
        while True:
            try:
                time.sleep(10)
                time_message = date.today()
                client.send(str(time_message).encode('ascii'))
            except:
                print(traceback.print_exc())
                self.clients.remove(client)
                client.close()
                break


    def client_handler(self,client,address):
        """
        Receives text message from the client and
        sends back the reversed text 
        
        """
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
        """
        Receives new client connection and creates 
        seperate threads to handle them 
        
        """


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

