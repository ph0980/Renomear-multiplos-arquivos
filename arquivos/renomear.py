'''
Este arquivo deve estar inserido no mesmo diretório dos arquivos que serão renomeados
'''
import os,time

def renomear(caminho=os.path.dirname(__file__)):
    identificador=input('Informe o identificador: ')
    identificador+=' ' if identificador!='' else ''
    mudarextensao=True if input('Deseja mudar a extensão ? (s/n)')=='s' else False
    if mudarextensao:
            extensao=input('Informe a nova extensão: ')
            extensao='.'+extensao
    numerar=True if input('Deseja numerar os arquivos ? (s/n)')=='s' else False
    if numerar:
        remover_nome=True if input('Deseja remover os nomes atuais ? (s/n)')=='s' else False 
    else:
        remover_nome=False
    programa=os.path.basename(__file__)
    arquivos=os.listdir(caminho)     
    if not confirmar(caminho):
        encerrar()
    else:
        try:
            i=1
            for arquivo in arquivos:
                if arquivo!=programa:
                    if not mudarextensao and numerar:
                        arq=arquivo.split('.')
                        extensao=arq[1]
                        extensao='.'+extensao
                        if remover_nome:
                            nomenovo=identificador+str(i)+extensao
                        else:
                            arq=arquivo[:-4]
                            nomenovo=identificador+arq+str(i)+extensao
                    elif mudarextensao and numerar:
                        nomenovo=identificador+str(i)+extensao
                    elif mudarextensao and not numerar:
                        nomenovo=identificador+arquivo+extensao
                    elif identificador!='':
                        nomenovo=identificador+arquivo
                    else:
                        break
                    os.rename(arquivo,nomenovo)
                    i+=1
                    print(arquivo+' renomeado para '+nomenovo)
            encerrar()       
        except Exception as e:
            print('Erro -> '+str(e))
    
def encerrar():
    print('encerrando',end=' ')
    for i in range(5,0,-1):
        print('.',end=' ')
        time.sleep(1)

def confirmar(caminho):
    programa=os.path.basename(__file__)
    arquivos=os.listdir(caminho)
    print('---------------------------------------------------------------------------------------------------')
    print('                                  Lista de arquivos encontrados                                    ')
    for arquivo in arquivos:
        if arquivo!=programa:
            print(arquivo)
    print('---------------------------------------------------------------------------------------------------')
    return True if input('Deseja renomear todos estes arquivos ? (s/n)')=='s' else False


if __name__ == '__main__': 
    print('                          Renomear multiplos arquivos simultaneamente                              ')
    print('---------------------------------------------------------------------------------------------------')
    print('|Este arquivo deve estar inserido em um diretório onde só existem os arquivos que serão renomeados|')
    print('---------------------------------------------------------------------------------------------------')
    renomear()
