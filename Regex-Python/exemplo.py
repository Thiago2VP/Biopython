import re

string = "O rato roeu a roupa do rei de Roma."

busca = re.search("[^ ]*[r|R][^ |.]*", string)
busca_completa = re.findall("[^ ]*[r|R][^ |.]*", string)

if busca_completa:
    print(busca_completa)
