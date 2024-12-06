from datetime import date, datetime

d = datetime.now()

#Formatando data e hora
print (d.strftime("%d/%m/%Y %H:%M"))

# convertendo string para datetime
date_string = "06/12/2024 13:33"
d1 = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print (d1)

data_hora_atual = datetime.now()
data_hora_str = "2024-12-6 13:45"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print (data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print (data_convertida)
