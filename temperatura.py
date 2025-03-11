class ControleTemperatura:
    def __init__(self, temperatura=0.0):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if isinstance(nova_temperatura, float):
            if -50 <= nova_temperatura <= 100:
                self.__temperatura = nova_temperatura
            else:
                print("Temperatura inválida! Deve estar entre -50 e 100 graus Celsius.")
        else:
            print("A temperatura deve ser um número.")
    
    def converter_para_fahrenheit(self):
        return self.__temperatura * 1.8 + 32

temp = ControleTemperatura()
temp.temperatura = 25.0
print(f"Temperatura em Celsius: {temp.temperatura}")
print(f"Temperatura em Fahrenheit: {temp.converter_para_fahrenheit()}")