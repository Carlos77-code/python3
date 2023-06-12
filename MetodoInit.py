# Quando o def está dentro da classe não é uma função é chamado de método
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Carlos', 'Lima')

p2 = Pessoa('Samuel', 'Fernandes')

p3 = Pessoa('Gabriel', 'Fernandes')

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)
print()
print(p3.nome)
print(p3.sobrenome)