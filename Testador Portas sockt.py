import socket
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[94mOlá vamos começar...\033[0m\n")
inicio = int(input("\033[33mDIGITE O INICIO DO RANGE:\033[0m" ))
fim = int(input("\033[33mDIGITE O FIM DO RANGE:\033[0m" ))
print("")
with open("ips.txt") as f:
    ips = f.read().splitlines()

with open("sucesso.txt", "a") as f:
    for ip in ips:
        host = ip
        for port in range(inicio, fim):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"\033[92m{ip} : {port} ABERTA\033[0m")
                f.write("Port {} on host {} is open\n".format(port, host))
            else:
                print(f"\033[33m{ip} : {port} fechada\033[0m")

            s.close()