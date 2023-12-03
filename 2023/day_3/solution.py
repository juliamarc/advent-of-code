import re

from collections import defaultdict

def is_symbol_adjacent(matrix, coord):
    row_num = coord[0]
    num_start = coord[1]
    num_end = coord[2]
    max_row = len(matrix)
    max_col = len(matrix[0])
    pattern = r'[\d\.]'

    adj_symbols = []
    # top
    if row_num-1 > 0:
        for i in range(num_start-1 if num_start-1 >= 0 else 0, num_end+1 if num_end+1 <= max_col else max_col):
            adj_symbols.append(re.match(pattern, matrix[row_num-1][i]))
    # bottom
    if row_num+1 < max_row:
        for i in range(num_start-1 if num_start-1 >= 0 else 0, num_end+1 if num_end+1 <= max_col else max_col):
            adj_symbols.append(re.match(pattern, matrix[row_num+1][i]))
    # left
    if num_start-1 > 0:
        adj_symbols.append(re.match(pattern, matrix[row_num][num_start-1]))
    # right
    if num_end < max_col:
        adj_symbols.append(re.match(pattern, matrix[row_num][num_end]))

    return not all(adj_symbols)

def get_symbol_adjacent_nums(matrix, coord, symbols_dict):
    row_num = coord[0]
    num_start = coord[1]
    num_end = coord[2]
    num = int(''.join((matrix[row_num][num_start:num_end])))
    max_row = len(matrix)
    max_col = len(matrix[0])
    pattern = r'[\d\.]'

    # top
    if row_num-1 > 0:
        for i in range(num_start-1 if num_start-1 >= 0 else 0, num_end+1 if num_end+1 <= max_col else max_col):
            if not re.match(pattern, matrix[row_num-1][i]):
                symbols_dict[(row_num-1, i)].append(num)
    # bottom
    if row_num+1 < max_row:
        for i in range(num_start-1 if num_start-1 >= 0 else 0, num_end+1 if num_end+1 <= max_col else max_col):
            if not re.match(pattern, matrix[row_num+1][i]):
                symbols_dict[(row_num+1, i)].append(num)
    # left
    if num_start-1 > 0:
        if not re.match(pattern, matrix[row_num][num_start-1]):
            symbols_dict[(row_num, num_start-1)].append(num)
    # right
    if num_end < max_col:
        if not re.match(pattern, matrix[row_num][num_end]):
            symbols_dict[(row_num, num_end)].append(num)

    return symbols_dict

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        matrix = list(map(list, lines))
        sum_adjacent = 0

        num_coords = []
        for row_num, line in enumerate(lines):
            for m in re.finditer(r'\d+', line):
                num_coords.append((row_num, m.start(), m.end()))

        for coord in num_coords:
            if is_symbol_adjacent(matrix, coord):
                sum_adjacent += int(lines[coord[0]][coord[1]:coord[2]])

    print("--- Part One ---", sum_adjacent, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        matrix = list(map(list, lines))
        sum_ratios = 0

        num_coords = []
        for row_num, line in enumerate(lines):
            for m in re.finditer(r'\d+', line):
                num_coords.append((row_num, m.start(), m.end()))

        symbols_dict = defaultdict(list)
        for coord in num_coords:
            get_symbol_adjacent_nums(matrix, coord, symbols_dict)

        for adj_num in symbols_dict.values():
            if len(adj_num) == 2:
                sum_ratios += adj_num[0]*adj_num[1]

    print("--- Part Two ---", sum_ratios, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
