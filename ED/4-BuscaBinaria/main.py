import csv
from typing import List
import timeit 

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
print(servidores_dns)

