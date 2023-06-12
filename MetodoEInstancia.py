#Um método nada mais é que uma função que está dentro da Classe, e usa o primeiro parâmetro Self

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerando(self):
            print(f'{self.nome} está acelerando...')
    
    def freiar(self):
         print(f'{self.nome} deve freiar antes que aconteça algo... ')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerando()
fusca.freiar()
print()
celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerando()
celta.freiar()