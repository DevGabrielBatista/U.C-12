
class midia:
    def __init__(self,titulo):
        self.titulo = titulo
        
    def exibir_info(self):
        
        raise NotImplementedError('subclasses deve implementar esse metodo')

class Livro(midia):
    def __init__(self,titulo,autor,num_paginas):
        super().__init__(titulo)
        self.autor=autor
        self.num_paginas=num_paginas

    def exibir_info(self):
        return print(f"livro{self.titulo} de {self.autor},com {self.num_paginas}paginas")
    
class filme(midia):
    def __init__(self,titulo,diretor,producao):
        super().__init__(titulo)
        self.diretor = diretor
        self.producao = producao

    def exibir_info(self):
        return print(f"um filme:{self.titulo},dirigido por {self.diretor}com {self.producao}de duramento")
    
class musica(midia):
     def __init__(self,titulo,artista,duracao):
        super().__init__(titulo)
        self.artista = artista
        self.duracao = duracao

     def exibir_info(self):
          return print(f"uma musica chamada:{self.titulo},com o artista  {self.artista}com {self.duracao}de duramento")

obj_1 = Livro(" as aventuras de poliana","damião",50)
obj_1.exibir_info()

obj_2 = filme( 'ate a ultima mulher', 'raspa canela ',' 120 minutos ')
obj_2.exibir_info()

obj_3 = musica(' tudo ',' daniel lucktive ',' 10 minutos ')
obj_3.exibir_info()


    
       

