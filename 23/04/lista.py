nomes = ["Bruno","Jessica","jhossatan","oi","tudo","bem","?"]
nominho = [nominho for nominho in nomes if nominho.lower().count("s")==2]
print(nominho)