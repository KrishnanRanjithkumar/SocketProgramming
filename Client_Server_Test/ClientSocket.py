import socket
import threading
import sys
import traceback
import ssl


class ClientSocket:

    

    def __init__(self, client=None):
        if client is None:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.context = ssl.create_default_context()
            self.context.check_hostname = False
            self.context.verify_mode = ssl.CERT_NONE
            self.client.connect(("127.0.0.1",3443))
            self.sslclient = self.context.wrap_socket(self.client, server_hostname="127.0.0.1")
            print(self.sslclient.version())
        else:
            self.sslclient = client
        
          
        
    def receive(self):
        received = ""
        while True:
            try:
                message = self.sslclient.recv(1024).decode('ascii')
                print(message)
                received = message
            except:
                print("An error occured ")
                print(traceback.print_exc())
                self.sslclient.close()
                break
        return received

    def send(self,msg):
        while True:
            try:
                message =  f'{input("")}'
                #self.sslclient.send(message.encode('ascii'))
                self.sslclient.send(msg.encode('ascii'))

            except:
                print("An error in  occured ")
                self.sslclient.close()
                break

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()

if __name__ == "__main__":
    client = ClientSocket()
    client.start()

    #receive_thread = threading.Thread(target=client.receive)
    #receive_thread.start()

    #send_thread = threading.Thread(target=client.send)
    #send_thread.start()

