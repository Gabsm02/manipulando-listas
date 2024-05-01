Lista_Vazia = []

Lista_Vazia.append(1)
Lista_Vazia.append(2)
Lista_Vazia.append(3)
Lista_Vazia.append('Valor')

len(Lista_Vazia) # 4

#Acessar
# Listas vazias começam com índice 0
Lista_Vazia[0] # 1
Lista_Vazia[0:2] # [1, 2]

#Zerar a lista
#Lista_Vazia.clear()

#Inserir um novo valor
Lista_Vazia.insert(0, 'Novo Valor') # ['Novo Valor', 1, 2, 3, 'Valor']

#Juntando listas
Lista_Vazia2 = [4, 5, 6]
Lista_Vazia.extend(Lista_Vazia2) # ['Novo Valor', 1, 2, 3, 'Valor', 4, 5, 6]

# Removendo um valor pelo nome
Lista_Vazia.remove('Valor') # ['Novo Valor', 1, 2, 3, 4, 5, 6]

# Removendo um valor pelo índice
Lista_Vazia.pop(0) # [1, 2, 3, 4, 5, 6]

# Ordenando uma lista
lista = [1, 5, 3, 2, 4]
lista.sort() # [1, 2, 3, 4, 5]

# Ordenando uma lista de forma reversa
lista.sort(reverse=True) # [5, 4, 3, 2, 1]

# Copiando uma lista
lista2 = lista.copy() # [5, 4, 3, 2, 1]

# Procurando a posicão de um valor
lista.index(3) # 2


