import os
import subprocess

# os.system("echo hello world")
# print("Parte 1")
# variavel = subprocess.call(["py", "list-operations.py"])
# variavel = subprocess.check_output(["py", "list-operations.py"])
# variavel = subprocess.check_output(["python3", "list-operations.py"])
# print("Parte 2")
# print(variavel)

os.system("blastp -query Quimicos/cirop.fasta -subject Quimicos/pcare.fasta > Quimicos/resultado-blast.txt")
os.system("blastp -query Quimicos/cirop.fasta -subject Quimicos/pcare.fasta -outfmt 6 > Quimicos/resultado-tabular-blast.txt")

linhas = open("resultado-tabular-blast.txt").readlines()
for linha in linhas:
    print(linha)
