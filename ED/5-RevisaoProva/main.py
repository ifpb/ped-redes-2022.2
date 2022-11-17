import random

from algoritmos_ordenacao import insertion_sort_bin, selection_sort_alg, mergesort, quicksort

from busca_sequencial import busca_sequencial, busca_sequencial_recursiva
from busca_binaria import busca_binaria, busca_binaria_recursiva


from pilha import Pilha
import csv
import sys


if __name__ == '__main__':
    if (len(sys.argv) <= 1 or sys.argv[1] == '1'):
        print("#### Q1 ####")
        numeros_aleatorios = random.sample(range(0,9999), 50)
        pilha = Pilha()
        for numero in numeros_aleatorios:
            pilha.push(numero)
        
        n = int(input("Quantos itens deseja processar?"))
        pilha.processar(n)

    if (len(sys.argv) <= 1 or (sys.argv[1] == '2' or sys.argv[1] == '3')):
        servidores_dns = []
        with open('dns_br.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader, None)  # pula os cabeçalhos
            for row in csv_reader:
                servidor_dns = dict()
                servidor_dns['ip'] = row[0]
                servidor_dns['nome'] = row[1]
                servidores_dns.append(servidor_dns)

        ordenado_1 = servidores_dns.copy()
        selection_sort_alg(ordenado_1, "ip")

        ordenado_2 = servidores_dns.copy()
        insertion_sort_bin(ordenado_2, "ip")

        ordenado_3 = servidores_dns.copy()
        mergesort(ordenado_3, "ip")

        ordenado_4 = servidores_dns.copy()
        quicksort(ordenado_4, "ip")

    if (len(sys.argv) <= 1 or sys.argv[1] == '2'):
        print("#### Q2 ####")
        print("Selection sort = ", ordenado_1)
        print("Insertion Sort = ", ordenado_2)
        print("Merge Sort = ", ordenado_3)
        print("Quick Sort = ", ordenado_4)
    
    if (len(sys.argv) <= 1 or sys.argv[1] == '3'):
        print("#### Q3 ####")

        print("Busca sequencial (iterativa) = ", busca_sequencial("45.233.172.10", ordenado_3.copy()))
        print("Busca sequencial (recursiva) = ", busca_sequencial_recursiva("45.233.172.10", ordenado_3.copy()))

        print("Busca binária (iterativa) = ", busca_binaria("45.233.172.10", ordenado_3.copy()))
        print("Busca binária (recursiva) = ", busca_binaria_recursiva("45.233.172.10", ordenado_3.copy()))