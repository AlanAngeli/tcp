import socket #biblioteca socket é para fazeer o relacionamento com placa de rede e sistema operacional
import sys #fornece acesse a algumas variaveis e funções com interações com o Python

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso')

    HostAlvo = input('Digite o Host ou IP a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com sucesso no Host: ' + HostAlvo + 'e na porta: ' + PortaAlvo)
        s.shutdown(2) #2 segundos pra fechar a conexão pra não ficar em loop
    except:
        print('Não foi possível conectar no Host: ' + HostAlvo + ' e na porta: ' + PortaAlvo)
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == "__main__": #se o nome da função for "main"...
    main() #...então, chame "main"