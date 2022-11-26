#Port Scanner

# OBS : Demora um pouco para o programa começar a mostrar as portas.


import pyfiglet 
import sys 
import socket 
from datetime import datetime 
   

ascii_banner = pyfiglet.figlet_format("SEGURANCA VF - PORT SCANER") 
print(ascii_banner) 

IP = input(str("DIGITE O IP: "))

print("-" * 20) 
print("IP: " + IP) 
print("DATA/HORA:" + str(datetime.now())) 
print("-" * 20) 

try: 
      
    
    for port in range(1,65535):  #mostra todas as portas do ip 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
        
        result = s.connect_ex((IP,port)) 
        if result ==0: 
            print("PORTA {} ABERTA".format(port)) 
        s.close() 
          
except socket.gaierror: 
        print("\n IP HOST NÃO VALIDO !!!!") 
        sys.exit() 
