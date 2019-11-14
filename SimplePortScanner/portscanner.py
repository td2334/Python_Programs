import socket
import sys 

#sys.argsv[0] = name of python script
#sys.argv = the first command line arguement
#syst.argv[2] = the second command line argeument 
#python3 scanner.py <ip> <port>

ip = sys.argv[1]
minport = int(sys.argv[2])
maxport = int(sys.argv[3])

for port in range(minport, maxport): 
	try:	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(.5) #wait half second before throwing 
		sock.connect((ip, port)) #line exception may occur on
		print("port is open" )
	
		sock.close()
	except socket.timeout:
		print("port is firewall")
	except socket.error:
		print("port is closed")