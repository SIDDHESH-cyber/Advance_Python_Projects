import socket
import os
import time

from termcolor import colored

url_color= colored('URL', 'cyan')
ip_color= colored('IP', 'cyan')

os.system('cls')

print(f"Welcome To {url_color} to {ip_color} Convertor\n")
print("This Format : www.google.com")

url=input("Enter Your Url As Above Shown : ")

os.system('cls')

print("Connecting To Your Server......")

time.sleep(3)

print("Gettig Ip Address....")

time.sleep(3)
os.system('cls')

s=socket.gethostbyname(url)

url_res= colored(url, 'cyan')
ip_res= colored(s, 'cyan')

print(f"This Is Your Ip For [ {ip_res} ] Given URL {url_res} ")
