import json
# caminho_arquivo = 'D:\\carlo\\Cursos\\Python\\Modulos\\ambiente_virtuais\\Projeto'
# caminho_arquivo += 'aula186.txt'

# with open(caminho_arquivo, 'w') as arquivo:
#     print('Arquivo vai ser fehcado')

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula190.json', 'w') as arquivo:
    json.dump(
        pessoa, arquivo, ensure_ascii=False,
        indent=2,
        )
