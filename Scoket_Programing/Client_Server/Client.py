import socket			
import os
import time

def main():
    s = socket.socket()	

    port = 12345
    try:
        s.connect(('127.0.0.1', port))
        print("Connection Established")
        time.sleep(5)
        os.system('cls')

        print("Wait For Message.......")

        time.sleep(3)
        os.system('cls')

        msg=(s.recv(1024).decode())
        print(msg)
    except:
        print("Re-Trying Please Wait.....")
        main()

if __name__ == "__main__":
    main()
