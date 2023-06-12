class Animal:
    def __init__(self, name):
        self.name = name

    def comendo(self, alimento):
        return f'{self.name} está roendo um {alimento}'

cachorro = Animal(name='Cachorro')
print(cachorro.name)
print(cachorro.comendo('osso'))

print()
class atitude:
    def __init__(self, correr):
        self.correr = correr
    
    def pular(self, pulou):
        return f'{pulou}'

pessoa = atitude(correr='correu')
print(f'O cachorro {pessoa.correr}, {pessoa.pular("pulou em um estranho")}')
print(pessoa.pular('pulou em seu dono'))
print(cachorro.name)