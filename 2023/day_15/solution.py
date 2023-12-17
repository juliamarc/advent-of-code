import re

from collections import defaultdict, OrderedDict
from functools import reduce

def part_1():
    with open('input') as file:
        init_seq = file.read().replace('\n', '').split(',')

        total = 0
        for step in init_seq:
            total += reduce(lambda a, b: (a + b)*17 % 256, map(ord, step), 0)

    print("--- Part One ---", total, sep='\n')

def part_2():
    with open('input') as file:
        init_seq = file.read().replace('\n', '').split(',')
        boxes = defaultdict(OrderedDict)
        for step in init_seq:
            matches = re.findall(r'(\w+)(-|=)(\d+)?', step)[0]
            label = matches[0]
            op_char = matches[1]
            focal_len = matches[2] if matches[2] else None
            box = reduce(lambda a, b: (a + b)*17 % 256, map(ord, label), 0)

            if op_char == '-' and label in boxes[box]:
                boxes[box].pop(label, None)
            elif op_char == '=':
                boxes[box][label] = focal_len

        total = 0
        for box, lenses in boxes.items():
            for i, lens in enumerate(lenses.items(), 1):
                total += (box + 1)* i * int(lens[1])

    print("--- Part Two ---", total, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
