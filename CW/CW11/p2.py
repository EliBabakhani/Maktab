import argparse

parser=argparse.ArgumentParser()

parser.add_argument('first_num', help="add first number")
parser.add_argument('second_num', help="add second number")

args=parser.parse_args()
print(f'sum: {int(args.first_num)+int(args.second_num)}')


