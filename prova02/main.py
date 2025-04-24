from pydoc import cli
from clinica import Clinica
from pet import Pets


clinica1 = Clinica("Marinho")

pet1 = Pets("Cavalo", "consulta")
pet2 = Pets("Cobra", "consulta")
pet3 = Pets("Cachorro", "vacina")
pet4 = Pets("Gato", "banho e tosa")

#adicionando os pets a fila
clinica1.checkIn(pet1)
clinica1.checkIn(pet2)
clinica1.checkIn(pet3)
clinica1.checkIn(pet4)
#Mostrar Pets
clinica1.mostrarPets()
clinica1.exibeQuantidade()
#Atender o Primeiro Pet
print(" ")
clinica1.AtendePet()
#Mostrando a fila Novamente
print(" ")
clinica1.exibeQuantidade()
print(" ")
clinica1.mostrarPets()
