import socket 
import sys 
import os 

sock = socket.socket()
ip_addr= sys.argv[1]
port = int(sys.argv[2])
sock.connect((ip_addr,port))

userinput = input("Enter Path Data: ")

"""
if len(lenofinput) != 3:
	print("# Args Requried")
"""

splituserinput = userinput.split(" ")
print(splituserinput)

"""
This section of code is for the get function
"""

def main():
	if splituserinput[0] == "GET": 

		print(splituserinput[0])		
		#create the file name
		sock.sendall(splituserinput[0].encode())
		sock.sendall(splituserinput[1].encode())
		print(splituserinput[2]) #testing 
	
	
		getfilename = splituserinput[2]
	
		filename = getfilename
		file = open(filename, 'wb')
		file_data = sock.recv(1024)
		file.write(file_data)
		file.close()
		print("Completed")

	elif splituserinput[0] == "PUT":
		
		print(splituserinput[0])		
		#create the file name
		sock.sendall(splituserinput[0].encode())
		sock.sendall(splituserinput[2].encode())

		print(splituserinput[2]) #testing 
		
		filename = splituserinput[1]
		file = open(filename, 'rb')
		file_data = file.read(1024)
		sock.sendall(file_data)
		print("file send")
	else:
		print("You must use GET or PUT")
main()

