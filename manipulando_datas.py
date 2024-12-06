"""
Podemos criar e manipular obnjetos date, time e datetime.
Podemos adicionar e subtrair datas, verificar a diferença entre as datas e muito mais
"""
from datetime import date, datetime, timedelta

# d = datetime(2024, 12, 6, 13, 1)
# print (d)

# d1 = d + timedelta(weeks = 1)
# print (d1) 


tipo_carro = input("Digite o modelo: ")
tempo_pequeno = 30
tempo_medio = 45
tempo_longo = 60
data_atual = datetime.now()

if tipo_carro == "milk":
    data_estimada = data_atual + timedelta(minutes= tempo_pequeno)
    print (f"O carro chegou : {data_atual} e ficara pronto as {data_estimada}")
elif tipo_carro == "way":
    data_estimada = data_atual + timedelta(minutes= tempo_medio)
    print (f"O carro chegou : {data_atual} e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes= tempo_longo)
    print (f"O carro chegou : {data_atual} e ficara pronto as {data_estimada}")