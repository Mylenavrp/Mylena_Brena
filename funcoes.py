#n = n dados a serem rolados
#lista = lista do valor de cada dado rolado
import random


dados_rolados = []
def rolar_dados(n):
    for i in range(n):
        valor_dado = random.randint(1,6)          #sorteio do valor do dado
        dados_rolados.append(valor_dado)
    return dados_rolados


#dados_rolados = valor dos n dados que foram rolados
#dados_no_estoque = dado que o jogador decidiu guardar
#dado_para_guardar = posição/indice do dado que será guardado

def  guardar_dado(dados_rolados,dados_no_estoque, dado_para_guardar):
    if not (0 <= dado_para_guardar < len(dados_rolados)):         #se o indice não for válido retorna as cópias
        return dados_rolados[:], dados_no_estoque[:]
    
    valor = dados_rolados[dado_para_guardar] #valor que será movimentado
    #remove o dado em dado_para_guardar
    novos_dadosrolados = (dados_rolados[:dado_para_guardar]+ dados_rolados[dado_para_guardar+1:])
    
    #adiciona ao novo estoque
    novo_estoque = dados_no_estoque + [valor]  
    return [novos_dadosrolados, novo_estoque]


def remover_dado(dados_rolados, dados_no_estoque,dado_para_remover):
    if not (0 <= dado_para_remover < len(dados_no_estoque)):         #se o indice não for válido retorna as cópias
        return dados_rolados[:], dados_no_estoque[:]
    
    
    valor = dados_no_estoque[dado_para_remover]

    #novo estoque sem o elemento 
    #novo_estoque é dados_no_estoque sem o valor removido
    novo_estoque = (dados_no_estoque[:dado_para_remover]+ dados_no_estoque[dado_para_remover+1:])

    #adiciona o valor no final de uma cópia de dados_rolados
    novos_rolados = dados_rolados[:] + [valor]

    return [novos_rolados,novo_estoque]
    #novos_rolados é a lista de dados_rolados com o valor adicionado no final


def calcula_pontos_regra_simples(faces):
    #conta quantas vezes cada face aparece 
    quantidade_faces = {}
    for valor in faces:
        quantidade_faces[valor] = quantidade_faces.get(valor, 0) + 1

    #para cada face(de 1 a 6) multiplica a quantidade de faces pelo valor da face
    pontos = {}
    for face in range(1,7):
        qtd = quantidade_faces.get(face,0)
        pontos[face] = qtd * face
    return pontos

def calcula_pontos_soma(faces):
    #soma os valores de todas as faces
    total = 0
    for valor in faces:
        total += valor
    return total

def calcula_pontos_sequencia_baixa(faces):
    #possíveis sequencias(1,2,3,4 - 2,3,4,5 - 3,4,5,6)
    #testa cada possível sequencia
    for inicio in(1,2,3):
        seq1 = seq2 = seq3 = seq4 = False
        for i in faces:
            if i == inicio:
                seq1 = True
            elif i == inicio +1:
                seq2 = True
            elif i == inicio +2:
                seq3 = True
            elif i == inicio +3:
                seq4 = True
            
            if seq1 and seq2 and seq3 and seq4:
                return 15
            
    return 0

def calcula_pontos_sequencia_alta(faces):
    #possíveis sequencias(1,2,3,4,5 - 2,3,4,5,6)
    for inicio in(1,2):
        seq1 = seq2 = seq3 = seq4 = seq5 = False
        for i in faces:
            if i == inicio:
                seq1 = True
            elif i == inicio +1:
                seq2 = True
            elif i == inicio +2:
                seq3 = True
            elif i == inicio +3:
                seq4 = True
            elif i == inicio +4:
                seq5 = True
            
            if seq1 and seq2 and seq3 and seq4 and seq5:
                return 30
    return 0

def calcula_pontos_full_house(faces):
    #conta quantas vezes cada face aparece na lista de 5 dados
    frequencia = {}      
    for face in faces:
        frequencia[face] = frequencia.get(face, 0)+1
    #full house tem exatamente 2 valores distintos
    if len(frequencia) != 2:
        return 0
    
    #testa se o valor aparece 3 vezes e o outro 2
    tem_tres = False
    tem_dois= False
    for qtd in frequencia.values():
        if qtd ==3:
            tem_tres = True
        elif qtd ==2:
            tem_dois = True
    #soma dos 5 dados
    if tem_tres and tem_dois:
        total = 0
        for face in faces:
            total += face
        return total
    return 0

def calcula_pontos_quadra(faces):
    #conta quantas vezes cada face aparece na lista de 5 dados
    frequencia = {}
    for face in faces:
        frequencia[face] = frequencia.get(face,0) + 1
    
    #se aparecer algum valor pelo menos 4 vezes, pontua na soma total
    for qtd in frequencia.values():
        if qtd >= 4:
            total = 0
            for i in faces:
                total += i
            return total
    return 0 

def calcula_pontos_quina(lista_de_dados):
    #conta quantas vezes um mesmo valor caiu
    dic={}
    for num in lista_de_dados:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    for contagem in dic.values():
        if contagem>=5:
            return 50
    return 0
        
def calcula_pontos_regra_avancada(lista_de_dados):
    dic={'cinco_iguais': calcula_pontos_quina(lista_de_dados),
    'full_house':calcula_pontos_full_house(lista_de_dados) ,
    'quadra': calcula_pontos_quadra(lista_de_dados),
    'sem_combinacao': calcula_pontos_soma(lista_de_dados) ,
    'sequencia_alta': calcula_pontos_sequencia_alta(lista_de_dados),
    'sequencia_baixa': calcula_pontos_sequencia_baixa(lista_de_dados)
}
    return dic   

