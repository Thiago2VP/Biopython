arquivo = open("Quimicos/ex-multi-fasta.fasta")

linhas = arquivo.readlines()
multifasta = {}

seq_atual = ""

for linha in linhas:

    if linha[0] == ">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = multifasta[seq_atual] + linha.strip()


print(multifasta)
