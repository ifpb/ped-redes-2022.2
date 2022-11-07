import csv
from typing import List
import timeit

from busca_sequencial import *
from busca_binaria import *

servidores_dns = []
with open('dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)  # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = dict()
    servidor_dns['ip'] = row[0]
    servidor_dns['nome'] = row[1]
    servidores_dns.append(servidor_dns)

servidores_dns.sort(key=lambda d: d["nome"])

print("#### Busca Sequencial (Iterativa) #### ")
print(busca_sequencial("telefonica", servidores_dns.copy()))
print("Tempo da busca sequencial iterativa = ", timeit.timeit("busca_sequencial(\"telefonica\", servidores_dns.copy())", setup="from __main__ import servidores_dns; from __main__ import busca_sequencial", number=1000))
print("#### Busca Sequencial (Recursiva) #### ")
print(busca_sequencial_recursiva("telefonica", servidores_dns.copy()))
print("Tempo da busca sequencial recursiva = ", timeit.timeit("busca_sequencial_recursiva(\"telefonica\", servidores_dns.copy())", setup="from __main__ import servidores_dns; from __main__ import busca_sequencial_recursiva", number=1000))
print("#### Busca Binária (Iterativa) #### ")
print(busca_binaria("TELEFONICA BRASIL S.A", servidores_dns.copy()))
print("Tempo da busca binária iterativa = ", timeit.timeit("busca_binaria(\"telefonica\", servidores_dns.copy())", setup="from __main__ import servidores_dns; from __main__ import busca_binaria", number=1000))
print("#### Busca Binária (Recursiva) #### ")
print(busca_binaria_recursiva("TELEFONICA BRASIL S.A", servidores_dns.copy()))
print("Tempo da busca binária recursiva = ", timeit.timeit("busca_binaria_recursiva(\"telefonica\", servidores_dns.copy())", setup="from __main__ import servidores_dns; from __main__ import busca_binaria_recursiva", number=1000))