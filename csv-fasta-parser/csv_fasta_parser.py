linhas = open("rcsb_pdb_sequence_20240108135529.csv").readlines()
fasta_novo = open("rcsb_pdb_sequence_20240108135529.txt", "a")
count = 0
for linha in linhas:
    if count > 1:
        linha_aux = linha.split('"')
        fasta_novo.write(">sp|"+linha_aux[11]+"|"+linha_aux[15]+" OX="+linha_aux[16][1:3]+linha_aux[16][4:])
        fasta_novo.write(linha_aux[13])
        fasta_novo.write("\n")
    count += 1
