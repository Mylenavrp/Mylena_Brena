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

                

