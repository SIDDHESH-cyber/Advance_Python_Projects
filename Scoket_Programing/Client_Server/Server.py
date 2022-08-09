import socket	

s = socket.socket()

print ("Socket successfully created")

port = 12345			

s.bind(('', port))		

print (f"Socket Binded to {port}")

s.listen(5)	

print ("Socket Is On Listening Mode.......")		

while True:
    c,addr = s.accept()	
    
    print ('Got connection From', addr )
    
    c.send(f'Thank you for connecting\n'.encode())
    
    c.close()
    
    break
	
