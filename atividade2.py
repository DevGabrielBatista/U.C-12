class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class carro(Veiculo):
    def __init__(self, marca, ano, num_portas):
        super().__init__(marca, ano)
        self.num_portas = num_portas
    def exibicao(self):
       print(f'O carro da marca {self.marca} do ano {self.ano} tem {self.num_portas} portas.')

novoCarro = carro('AAA', 2000, 4)
novoCarro.exibicao() 
    
class moto(Veiculo):
    def __init__(self, marca, ano, guidao):
        super().__init__(marca, ano)
        self.guidao = guidao
    def exibicao(self):
       print(f'A moto da marca {self.marca} do ano {self.ano} tem guidao do tipo {self.guidao}.')

moto1 = moto('honda',2017,'esportivo')
moto1.exibicao()

