"""
O que é o modulo datetime?
O modulo datetime em python é usado para lidar com datas e horas. Ele possui várias classes
uteis como date, time e timedelta
"""

from datetime import date, datetime

d = date(2024, 12, 3)
print (d)
print (date.today())

data_hora = datetime(2024, 12, 3, 12, 52)
print (data_hora)

