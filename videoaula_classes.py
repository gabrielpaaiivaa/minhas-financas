# Nova forma de criar classes em Python
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f'Meu nome é {self.nome}, tenho {self.idade} anos e meu email é {self.email}')

registro = Cliente(nome='Gabriel', email='gabriel@gmail.com', idade=18)

registro.exibir()