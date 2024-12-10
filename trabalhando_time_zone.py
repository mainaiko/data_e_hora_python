"""
trabalhando com fuso horarios
python facilita isso atraves do modulo "pytz"
permitir armazenar utc no banco de dados para mudança de fuso facilmente
"""

import pytz
from datetime import datetime, date

data = datetime.now(pytz.timezone("Europe/Oslo"))
data_1 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print (data)
print (data_1)




