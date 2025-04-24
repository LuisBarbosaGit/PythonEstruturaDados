class Armazem:
    def __init__(self, nome):
        self.nome = nome
        self.caixas = []
        self.estoque = []

    def AdicionaCaixa(self, caixa):
        self.caixas.append(caixa)
        print("Caixa armazenada")

    def AdicionaMaterial(self, material):
        self.estoque.append(material)

    def exibeArmazem(self):
        print(f"A quantidade de caixas em estoque é {len(self.estoque)}")

    def OrganizaMateriais(self):
        for materiais in self.estoque:
            for caixa in self.caixas:
                if caixa.tipo == materiais.tipo:
                    caixa.material.append(materiais)
        


