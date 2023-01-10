import os
from queue import PriorityQueue
import time
def clear(): return os.system('cls')

""" Estrutura de Dados """
vizinhos = {
    'Aveiro': {
        'Porto': 68,
        'Viseu': 95,
        'Coimbra': 68,
        'Leiria': 115
    },
    'Braga': {
        'Viana do Castelo': 48,
        'Vila Real': 106,
        'Porto': 53
    },
    'Bragança': {
        'Vila Real': 137,
        'Guarda': 102
    },
    'Beja': {
        'Évora': 78,
        'Faro': 152,
        'Setúbal': 142
    },
    'Castelo Branco': {
        'Coimbra': 159,
        'Guarda': 106,
        'Portalegre': 80,
        'Évora': 203
    },
    'Coimbra': {
        'Viseu': 96,
        'Leiria': 67,
        'Aveiro': 68,
        'Castelo Branco': 159
    },
    'Évora': {
        'Lisboa': 150,
        'Santarém': 117,
        'Portalegre': 80,
        'Setúbal': 103,
        'Beja': 78,
        'Castelo Branco': 203
    },
    'Faro': {
        'Setúbal': 249,
        'Lisboa': 299,
        'Beja': 152
    },
    'Guarda': {
        'Vila Real': 157,
        'Viseu': 85,
        'Castelo Branco': 106,
        'Bragança': 202
    },
    'Leiria': {
        'Lisboa': 129,
        'Santarém': 70,
        'Coimbra': 67,
        'Aveiro': 115
    },
    'Lisboa': {
        'Santarém': 78,
        'Setúbal': 50,
        'Leiria': 129,
        'Faro': 299,
        'Évora': 150
    },
    'Portalegre': {
        'Castelo Branco':80,
        'Évora':131
        },
    'Porto': {
        'Viana do Castelo': 71,
        'Vila Real': 116,
        'Viseu': 133,
        'Braga': 53,
        'Aveiro': 68
    },
    'Santarém': {
        'Évora':117,
        'Leiria':70,
        'Lisboa':78
        },
    'Setúbal': {
        'Beja':142,
        'Évora':103,
        'Faro':249,
        'Lisboa':50
        },
    'Viana do Castelo': {
        'Braga':48,
        'Porto':71
        },
    'Vila Real': {
        'Viseu': 110,
        'Braga': 106,
        'Bragança': 137,
        'Guarda': 157,
        'Porto': 116
    },
    'Viseu': {
        'Aveiro': 95,
        'Coimbra': 96,
        'Guarda': 85,
        'Porto': 133,
        'Vila Real': 110
    }
}

''' Distâncias '''
distancia = {
    'Aveiro': 366,
    'Braga': 454,
    'Bragança': 487,
    'Beja': 99,
    'Castelo Branco': 280,
    'Coimbra': 319,
    'Évora': 157,
    'Faro': 0,
    'Guarda': 352,
    'Leiria': 278,
    'Lisboa': 195,
    'Portalegre': 228,
    'Porto': 418,
    'Santarém': 231,
    'Setúbal': 168,
    'Viana do Castelo': 473,
    'Vila Real': 429,
    'Viseu': 363
}

''' Validar Cidade, verifica se existe'''
def validarcidade(nome):
    if nome in distancia.keys():
        return 1
    else:
        print('Ponto de Partida inexistente!')
        time.sleep(2)
        return 0


''' Função que devolve o caminho mais curto em linha reta para Faro dentro de um nó 
e também a dist entre cidades'''

def devolvemaiscurto(nome):
    maiscurto = 0
    distentrecidade = 0
    cidade = ''
    for y in vizinhos[nome].keys():
        if (nome == 'Faro'):
            cidade = nome
            maiscurto = distancia[nome]
            distentrecidade = 0
            return cidade, maiscurto, distentrecidade
        elif y == 'Faro':
            distentrecidade = vizinhos[nome][y]
            cidade = y
            maiscurto = distancia[y]
            return cidade,maiscurto,distentrecidade
        elif (maiscurto == 0):
            maiscurto = distancia[y]
            distentrecidade = vizinhos[nome][y]
            cidade = y
        elif (maiscurto > distancia[y]):
            maiscurto = distancia[y]
            distentrecidade = vizinhos[nome][y]
            cidade = y

    return cidade, maiscurto, distentrecidade




'''Profundidade Limitada'''


array=[]
def getfilho(origem,count,destino,x):
    if count<1:
        print("DESTINO IMPOSSIVEL")
        return None
    conta=(count-x)*(-1)
    if(len(array)!=conta):
        array[conta]= origem
    else:
        array.append(origem)
    global aux1
    aux1=origem
    for aux1 in vizinhos[aux1].keys():
        if(aux1!=destino):
            getfilho(aux1,count-1,destino,x)
        else:
            array.append(destino)
            print("DESTINO NAO IMPOSSIVEl")
            print("CAMINHO: ",array)
            print("CHEGOU AO DESTION")
        if(aux1==destino):
        	break     	
 


'''Função que devolve nó com menor custo'''
def devolvemenorcusto(nome):
    custo = 0
    cidade = ''
    for y in vizinhos[nome].keys():
        if custo == 0:
            custo = vizinhos[nome][y]
        elif custo > vizinhos[nome][y]:
            custo = vizinhos[nome][y]
            cidade = y
        
    return cidade, custo


'''Procura Sofrega'''
def procuraSofrega(pPartida, destino='Faro' , dist=0):
    caminho = []
    caminho.append(pPartida)
    if (pPartida == destino):
        print('Já se encontra em Faro.') 
    else:
        cidade = pPartida
        print('""""""""""""""Caminho Percorrido""""""""""""')
        while(True):
            if(cidade == destino):
                break
            if dist == 0:
                dist = devolvemaiscurto(cidade)[2]
            else:
                cidade = devolvemaiscurto(cidade)[0]
                caminho.append(cidade)
                dist += (devolvemaiscurto(cidade)[2])
                
                
    print('Caminho percorrido: ')     
    print(*caminho, sep=(' -> '))
    print('Distância Total: '+ str(dist) + ' km')
    time.sleep(4)

'''Usada na Procura A*'''
def getDistancia(lista):
        val = 0
        for i in range(len(lista) - 1):
            val += vizinhos[lista[i]][lista[i + 1]]
        return val

'''Procura A*'''
def Aestrela(origem, destino='Faro'): 
    resultado = PriorityQueue() 
    resultado.put((0,[origem])) 
    while True:
        current = resultado.get() 
        currentCity = current[1][-1] 
        currentValue = current[0]
        if destino == currentCity: 
            return current
        for city in vizinhos[currentCity].keys():
            resultado.put((getDistancia(current[1]) + vizinhos[currentCity][city] + distancia[city], current[1]+[city])) 

'''Custo Uniforme*'''            
def custoUniforme(origem, destino='Faro'): 
    resultado = PriorityQueue()
    resultado.put((0,[origem])) 
    while True:
        current = resultado.get() 
        currentCity = current[1][-1] 
        currentValue = current[0]
        if destino == currentCity: 
            return current
        for city in vizinhos[currentCity].keys():
            resultado.put((currentValue + vizinhos[currentCity][city], current[1]+[city]))
    
        

while (True):
    print("\n********************MENU********************")
    op = int(input('''    1 - Mostrar todas as cidades
    2 - Profundidade Limitado
    3 - Custo uniforme
    4 - Procura Sofrega
    5 - A*
    0 - Sair\n
Escolha uma opcao: '''))
    if op == 0:
        break
    elif op == 1:
        for city in distancia.keys():
            print(city)
        time.sleep(2)
    elif op == 2:
        c = input('Escolha o ponto de partida: ')
        x = validarcidade(c)
        d = input('Escolha o ponto de destino: ')
        x2 = validarcidade(d)
        if x == 1 and x2==1:
            n = int(input('Escolha o numero de interações: '))
            getfilho(c,n,d,n)
           
    elif op == 3:
        c = input('Escolha o ponto de partida: ')
        x = validarcidade(c)
        if x == 1:
            print(custoUniforme(c))
            time.sleep(5)  
    elif op == 4:
        c = input('Escolha o Ponto de Partida: ')
        x = validarcidade(c)
        print(x)
        if x == 1:
            procuraSofrega(c)
    elif op == 5:
        c = input('Escolha o ponto de partida: ')
        x = validarcidade(c)
        if x == 1:
            print(Aestrela(c))
            time.sleep(5)  

    else:
        print('Opção inválida. Escolha uma opção entre 1-5')
