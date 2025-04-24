from operator import indexOf
class Clinica:
    def __init__(self, nome):
        self.nome =  nome
        self.fila = []
    
    def checkIn(self, Pet):
        self.fila.append(Pet)
    
    def AtendePet(self):
        animal = self.fila[0].nome
        self.fila.pop(0)
        print(f"Animal {animal} atendido com sucesso!!")

    def mostrarPets(self):
        for pets in self.fila:
            print(f"Nome do animal: {pets.nome} \n Tipo de Atendimento: {pets.atendimento}")

    def exibeQuantidade(self):
        if len(self.fila) != 0:
            print(f"Quantidade aguardando {len(self.fila)}")
        else:
            print("Não há petz aguardando atendimento")