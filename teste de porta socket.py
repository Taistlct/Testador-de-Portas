import socket
import re
import time

sucesso = False
loggin_found = False

def le_arquivo(arquivo, modo):
    arq = open(arquivo, modo)
    retorno = arq.readlines()
    arq.close()
    return retorno

lista_ip = le_arquivo(r'C:\\Testador Portas\ip.txt', "r")
lista_portas = le_arquivo( r'C:\\Testador Portas\portas.txt', "r")


portas = []
# limpa as senhas da lista
for porta in lista_portas:
    porta = re.sub('\n$', '', porta)
    portas.append(porta)

ips = []
# limpa a lista de usuarios
for ip in lista_ip:
    ip = re.sub('\n$', '', ip)
    ips.append(ip)
# variavel que vai armazenar as senhas ativas
portas_ativas = []

def pega_ativas(senhas, senhas_ativas):
    i = 0
    padrao = 10
    global tamanho 
    tamanho = len(senhas)
    print("Total de Portas:{}".format(tamanho))
    if (padrao > tamanho):
        padrao = tamanho
    while i < padrao:
        if (senhas[i]):
            senhas[i] = re.sub('\n$', '', senhas[i])
            senhas_ativas.append(senhas[i])
        else:
            break
        i += 1
def remove_ativas(ativas, senhas):
    for porta in ativas:
        senhas.remove(porta)

def salva_sucesso(usuario, senha, status):
    fs = open(r"C:\\Testador Portas\sucesso.txt", "a")
    texto = "\n{}:{} |{}\n".format(usuario, senha, status)
    fs.write(texto)    
    fs.close()


def achada(status):
    print ("IP:", ip ,"PORTA:", porta ,'+--ATIVA--+')
    print (" ")    
    salva_sucesso(ip, porta, status)
    time.sleep(1)
    global sucesso
    sucesso = True  




def test_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    sockt0 = "TCP"
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sockt01 = "UDP"
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    result1 = sock1.connect_ex((ip,port))
    sock.close()
    global loggin_found
    try:
        if result == 0:
            achada(sockt0)  
    except:
        if result1 == 0:
            achada(sockt01)

tamanho_loop = len(portas)
tentativas = 0

while tamanho_loop > 0:
    # pega as próximas senhas a serem testadas 
    pega_ativas(portas, portas_ativas)               
    for ip in ips:        
        if ip in ips:
            for porta in portas_ativas:    
                try:                    
                    tentativas += 1
                    porta = int(porta)                                     
                    test_port(ip, porta)                                                         
                    if sucesso is True:           
                        sucesso = False
                    else:
                        print ("IP:", ip ,"PORTA:", porta," incorretos", "tentativas:", tentativas)             
                except :                     
                    print ("IP:", ip ,"PORTA:", porta," incorretos", "tentativas:", tentativas)                           
                                         
        else:                       
            print ("IP:", ip ,"PORTA:", porta," incorretos")

    remove_ativas(portas_ativas, portas)
    portas_ativas = []

    if tamanho == 0:
        print('Todas as portas foram testadas !!!')
        break


    # esvazia a lista de senhas ativas



