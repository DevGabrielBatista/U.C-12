class Funcionarios:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.__salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError('Subclasses devem implementar esse método')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

class Gerente(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.bonus = 0.2

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * self.bonus)

class Desenvolvedor(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.bonus = 0.1

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * self.bonus)

class Estagiario(Funcionarios):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_salario(self):
        return self.salario_base

class Modelo:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        return self.funcionarios

class Visao:
    @staticmethod
    def exibir_funcionario(funcionario):
        print(f"Nome: {funcionario.nome}, Cargo: {funcionario.__class__.__name__}, Salário: {funcionario.calcular_salario()}")

    @staticmethod
    def exibir_todos_funcionarios(funcionarios):
        for funcionario in funcionarios:
            Visao.exibir_funcionario(funcionario)

class Controlador:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

    def adicionar_funcionario(self, funcionario):
        self.modelo.adicionar_funcionario(funcionario)

    def listar_funcionarios(self):
        funcionarios = self.modelo.listar_funcionarios()
        self.visao.exibir_todos_funcionarios(funcionarios)

if __name__ == "__main__":
    modelo = Modelo()
    visao = Visao()
    controlador = Controlador(modelo, visao)

    while True:
        nome = input("Digite o nome do funcionário: ")
        salario_base = float(input("Digite o salário base do funcionário: "))
        cargo = input("Digite o cargo do funcionário (gerente, gesenvolvedor, estagiario): ")

        if cargo.lower() == "gerente":
            funcionario = Gerente(nome, salario_base)
        elif cargo.lower() == "desenvolvedor":
            funcionario = Desenvolvedor(nome, salario_base)
        elif cargo.lower() == "estagiario":
            funcionario = Estagiario(nome, salario_base)
        else:
            print("Cargo inválido. Tente novamente.")
            continue

        controlador.adicionar_funcionario(funcionario)

        continuar = input("deseja adicionar outro funcionário? (s/n): ")
        if continuar.lower() != 's':
            break

    controlador.listar_funcionarios()

