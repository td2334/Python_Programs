#Create Server that has open port


import socket #lets us use sockets 
import threading
ip = "127.0.0.1" #The ip address that the server will listen on 
port = 3306	#The port our server will listen on 


def connHandler(conn):
	print("Some Connected!")

def main():
	
	srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#srv.bind takes a tuple as an arguement 
	#first element is a string 
	#second element of tuple is a int
	
	srv.bind((ip, port)) 
	
	srv.listen(1) #Number of connections allowed 
	
	while True:
		#blocking will cause script to hang until a connection comes in.
		
		clientSock,address = srv.accept() 
		handler = threading.Thread(target=connHandler,args=(clientSock,))
		handler.start()
		
	
	

main()