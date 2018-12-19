import socket
import IndividualStock as stock
import Email as email
import CallAndMessage as cm
import Grammar as grammar
#import Lights as lights

class Connect(object):

    services  = ["Stock","SMS","Email","Call","Definition","Synonym","Pizza"]
    def __init__(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Socket cannot be created")
        host = "192.168.1.136"
        port = 9058
        self.serversocket.bind((host,port))
        self.serversocket.listen(5)
        print('server started and listening')

    def listen(self):
        (clientsocket, address) = self.serversocket.accept()
        while True:
            #(clientsocket, address) = self.serversocket.accept()
            print("Connection found")
            try:
                data = clientsocket.recv(1024).decode("utf-8")
                print(data)
                processed_action = data.split(",")
                function = processed_action[0]
                myinput = processed_action[1]
                print("My input: "+ myinput)

                if function == "Stock":
                    stock_info = stock.findStock(myinput)
                    clientsocket.send((stock_info + "\n").encode("utf-8"))
                    print("Sent stock information " + stock_info )
                elif function == "Email":
                    #Read text file, write input from Unity into text file
                    #message = processed_action[2]
                    email.emailBody(myinput)
                    email.main()
                    confirmation = "Email has been sent"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif function == "Call":
                    #Read in message if user calls or sends message
                    #message = processed_action[2]
                    #cm.outgoingCall(myinput,message)
                    cm.outgoingCall(myinput)
                    confirmation = "Called Phone"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif function == "SMS":
                    message = processed_action[2]
                    cm.sendMessage(myinput,message)
                    confirmation = "SMS message has been sent"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif function == "Definition":
                    grammar.Definition(myinput)
                    confirmation = "Found defintion"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif function == "Synonym":
                    grammar.Synonym(myinput)
                    confirmation = "Found synonym"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif function == "Pizza":
                    pizza.placeOrder(myinput)
                    confirmation = "Ordered Pizza (with TBD)"
                    #clientsocket.send(confirmation.encode("utf-8"))
                '''elif function == "Light":
                    lights.turnOn()
                    confirmation = "Adjust Hue Light"
                    #clientsocket.send(confirmation.encode("utf-8"))
                elif data == "ping":
                    print ("Unity Sent: " + str(data))
                    #clientsocket.send("pong")
                print("closed socket")'''
            finally:
                pass
                #clientsocket.close()
def main():
    connect = Connect()
    connect.listen()

if __name__ =='__main__':
    main()
