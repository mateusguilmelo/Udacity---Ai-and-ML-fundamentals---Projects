# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for i in range(20):
    print(data_list[i+1])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(20):
    print (data_list[i][6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    for colum in range(len(data)):
         column_list.append(data[colum][index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for i in range(len(data_list)):
    if data_list[i][-2] == "Male":
        male += 1
    elif data_list[i][-2] == "Female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

"""
      Função count_gender
      Essa função conta a quantidade de cada gênero na lista "data_list"
      Argumentos:
          data_list: banco de dados completo.
      Retorna:
          uma lista composta por [número de homens, número de mulheres]

"""

def count_gender(data_list):
    male = 0
    female = 0
    for i in range(len(data_list)):
        if data_list[i][-2] == "Male":
            male += 1
        elif data_list[i][-2] == "Female":
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

"""
      Função most_popular_gender
      Essa função retorna o genero que mais aparece no banco de dados data_list
      Argumentos:
          data_list: banco de dados completo
      Retorna:
          uma string com o nome do genero mais presente no banco de dados, podendo ser "Male" ou "Female".

"""

def most_popular_gender(data_list):
    male = count_gender(data_list)[0]
    female = count_gender(data_list)[1]
    if male > female:
        answer = "Male"
    else:
        answer = "Female"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

"""
      Função count_types
      Essa função conta a quantidade de cada tipo de cliente, podendo eles serem constumers ou subscribers
      Argumentos:
          data_list: banco de dados completo.
      Retorna:
          uma lista composta por [costumer, subscriber]

"""

def count_types(data_list):
    custumer = 0
    subscriber = 0
    for i in range(len(data_list)):
        if data_list[i][-3] == "Customer":
            custumer += 1
        elif data_list[i][-3] == "Subscriber":
            subscriber += 1
    return [custumer, subscriber]


user_types_list = column_to_list(data_list, -3)
user_types_titles = ["Custumer", "Subscriber"]
quantity = count_types(data_list)
y_pos = list(range(len(user_types_titles)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, user_types_titles)
plt.title('Quantidade por Tipos')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição é errada porque len(data_list) retorna o tamanho total \n da lista, porém, várias posições da lista não tem a posição gender respondida"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

for i in range(len(trip_duration_list)):
    trip_duration_list[i] = int(trip_duration_list[i])

#Associando as veriáveis aos primeiros valores da lista

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[0]
mean_trip = 0.
median_trip = 0.

#criando um iterador

"""
      Função my_range
      Essa função cria um iterador que vai de 0 até o tamanho da lista
      Argumentos:
          ordinary_list: qualquer lista ordinária
      Retorna:
          um iterador j por vez

"""

def my_range(ordinary_list):
    j = 0
    while j < len(ordinary_list):
        yield j
        j += 1

#encontrando o mínimo
for j in my_range(trip_duration_list):
    if min_trip > trip_duration_list[j]:
        min_trip = trip_duration_list[j]

#encontrando o máximo
for j in my_range(trip_duration_list):
    if max_trip < trip_duration_list[j]:
        max_trip = trip_duration_list[j]

#calculando a média
total_duration = 0.

for i in range(len(trip_duration_list)):
    total_duration += int(trip_duration_list[i])

mean_trip = round(total_duration/len(trip_duration_list))

#ordenando a lista e encontrando a mediana
ordinary_list = sorted(trip_duration_list)
is_it_even = len(ordinary_list)

if is_it_even % 2 == 0:
    median_trip = (ordinary_list[is_it_even / 2] + ordinary_list[is_it_even/2 +1]) / 2
else:
    median_trip = ordinary_list[int(is_it_even / 2) + 1]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_station_full_list = column_to_list(data_list, 3)
start_stations = set(start_station_full_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")

answer = "no"

answer = input("")

"""
      count_items
      conta o número de elementos diferentes em uma lista
      Argumentos:
          column_list: uma coluna de uma lista
      Retorna:
          item_types = lista com os elementos diferentes
          count_items = lista com o número 1 para cada elemento da column_list

"""

def count_items(column_list):
    item_types = []
    count_items = []
    for gender in column_list:
        if gender not in item_types:
            item_types.append(gender)
            count_items.append(1)
        else:
            i = item_types.index(gender)
            count_items[i] += 1

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
