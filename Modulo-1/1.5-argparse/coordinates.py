import argparse

parser = argparse.ArgumentParser()

# parâmetro nargs=2 permite que o argumento aceite 2 valores
### (nargs = '+') aceita um ou mais valores
### (nargs = '*') aceita zero ou mais valores
parser.add_argument('coord', nargs = 2)

# parâmetro required=True torna obrigatório fornecer a opção
# parâmetro help define a mensagem apresentada pela opção -h/--help
parser.add_argument('-t', '--tipo', required = True,
help ='Tipo da coordenada: polar ou cartesiana')

# parâmetro choices permite definir um conjunto de valores possíveis
parser.add_argument('-e', '--eixo', choices=['x', 'y', 'z'], default='z')
parser.add_argument('-n', '--num_pontos', choices=range(1,4))

args = parser.parse_args()
print(args)