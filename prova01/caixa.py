class caixa:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.limite = 30
        self.material = []
    
    def addMaterial(self, item):
        if len(self.material) < self.limite:
            self.material.append(item)
            print("Material Adicionado com sucesso")
        else:
            print("A caixa esta cheia")

    def retiraMaterial(self):
        self.material.pop()
        print("Material retirado com sucesso") 

    def exibeCaixa(self):
        i = 1
        print("Materiais na caixa:")
        for materiais in self.material:
            print(f"Material: {i} \nNome: {materiais.nome}") 
            print(f"Tipo: {materiais.tipo}")
            i+=1

    def qtdeMaterial(self):
        print(f"Quantidade de materiais na caixa {len(self.material)}") 

    def caixaVazia(self):
        if len(self.material) == 0:
            print("A caixa esta vazia")
        else:
            print("A caixa nao esta vazia")   

           