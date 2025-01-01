import argparse

parser = argparse.ArgumentParser()
# argumento posicional
parser.add_argument("filename")
# opção que espera um parâmetro inteiro
parser.add_argument("-r", "--row", type=int, default=0)
# opção interruptor liga/desliga
parser.add_argument("-i", "--inverted", action="store_true")

args = parser.parse_args()

with open(args.filename, 'r') as fp:
    rows = fp.readlines()
    if args.inverted:
        print(rows[args.row][::1])
    else:
        print(rows[args.row])