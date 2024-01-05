from Bio.Seq import Seq
from Bio import SeqIO
from Bio.PDB import *

# Declarar sequência
minha_primeira_sequencia = Seq("ATG")
# Complementar de uma sequência
seq_complementar = minha_primeira_sequencia.complement()
# Reverso Complementar de uma seguência
seq_complementar_reversa = minha_primeira_sequencia.reverse_complement()
# Transcrição
seq_rna = minha_primeira_sequencia.transcribe()
# Transcrição reversa
seq_dna = seq_rna.back_transcribe()
# Tradução (usado para a proteina)
seq_proteina = seq_rna.translate()

print("Sequência: ", end="")
print(minha_primeira_sequencia)
print("Complemento: ", end="")
print(seq_complementar)
print("Complemento Reverso: ", end="")
print(seq_complementar_reversa)
print("Transcrição: ", end="")
print(seq_rna)
print("Transcrição Reversa: ", end="")
print(seq_dna)
print("Tradução: ", end="")
print(seq_proteina)

for fasta in SeqIO.parse("pheromone.fasta", "fasta"):
    print(fasta.id)
    print(fasta.seq)

parser = PDBParser()
estrutura = parser.get_structure("1BGA", "1bga.pdb")
atomo_100 = estrutura[0]['A'][100]['CA']
atomo_101 = estrutura[0]['A'][101]['CA']
# Distância euclidiana
distancia = atomo_101 - atomo_100
print(distancia)
