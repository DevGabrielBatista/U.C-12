class Contabancaria:
    total_contas = 0
    taxa_juros = 0.05

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        Contabancaria.total_contas += 1

    def pessoa_f(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"


class PessoaFisica(Contabancaria):
    def __init__(self, titular, cpf, saldo=0):
        super().__init__(titular, saldo)
        self.cpf = cpf

    def pessoa_f(self):
        return f"Titular: {self.titular}, CPF: {self.cpf}, Saldo: {self.saldo}"


class PessoaJuridica(Contabancaria):
    def __init__(self, titular, cnpj, saldo=0):
        super().__init__(titular, saldo)
        self.cnpj = cnpj

    def pessoa_f(self):
        return f"Titular: {self.titular}, CNPJ: {self.cnpj}, Saldo: {self.saldo}"



conta_pf = PessoaFisica("Gabriel", "123.456.789-00", 1000)
conta_pj = PessoaJuridica("mauricio", "12.345.678/0001-99", 5000)

print(conta_pf.pessoa_f())
print(conta_pj.pessoa_f())


