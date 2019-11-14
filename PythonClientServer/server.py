#Create Server that has open port
import socket #lets us use sockets 
import threading
import os
import sys 

ip = "0.0.0.0" #The ip address that the server will listen on 
port = int(sys.argv[1]) 	#The port our server will listen on 


def connHandler(conn):
	command = conn.recv(1024).decode().strip()
	print(command)
	print(len(command))
	filepath = conn.recv(1024).decode()
	print(filepath)

	if command =="GET":
	
		print("Connected")		
		file = open(filepath, 'rb')
		print("file open")
		file_data = file.read(1024)
		print("file read")
		conn.sendall(file_data)
		print("File got")
		

	elif command =="PUT":
	
		filename = filepath
		file = open(filename, 'wb')
		file_data = conn.recv(1024).decode()
		file.write(file_data)
		file.close()
		print("Completed")

	else:
		for letter in command:
			print(letter)
	
		print("-----")
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
