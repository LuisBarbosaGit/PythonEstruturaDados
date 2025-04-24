from caixa import caixa
from material import material
from armazem import Armazem

#Criando Materiais
material1 = material("papel", "folha")
material2 = material("plastico", "garrafa de agua")
material3 = material("papel", "panfleto")
#Exibindo Materais
material1.exibeMaterial()
material2.exibeMaterial()
#Criando Caixa
caixapapel =  caixa("caixaPapel", "papel")
caixaplastico = caixa("Caixa de Plastico", "plastico")

armazem1 = Armazem("Reciclagem do Luis")
#Adiciona as caixas e os materias ao armazem
armazem1.AdicionaCaixa(caixapapel)
armazem1.AdicionaCaixa(caixaplastico)
armazem1.AdicionaMaterial(material1)
armazem1.AdicionaMaterial(material2)
#organiza o armazem, colocando cada material em sua caixa
armazem1.OrganizaMateriais()
#Exibe os materiais na caixa
caixapapel.exibeCaixa()
caixaplastico.exibeCaixa()
