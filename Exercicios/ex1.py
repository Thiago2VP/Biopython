import os

os.system("blastp -query beta_glucosidase.fasta -subject rcsb_pdb_sequence_20240108135529.txt -outfmt=6 > resultado_ex1.txt")
