import re
import itertools

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        galaxies, empty_rows, empty_columns = [], [], []
        for i, x in enumerate(lines):
            if len(x) == x.count('.'):
                empty_rows.append(i)

            for j, y in enumerate(x):
                if y == '#':
                    galaxies.append((i, j))

        lines_transposed = list(zip(*lines))
        for i, x in enumerate(lines_transposed):
            if len(x) == x.count('.'):
                empty_columns.append(i)

        result = sum(map(
            lambda p: \
                abs(p[0][0]-p[1][0]) + \
                abs(p[0][1]-p[1][1]) + \
                sum(1 for x in empty_rows if (x > min(p[0][0], p[1][0])) and (x < max(p[0][0], p[1][0]))) + \
                sum(1 for y in empty_columns if (y > min(p[0][1], p[1][1])) and (y < max(p[0][1], p[1][1]))),
            itertools.combinations(galaxies, 2)))

    print("--- Part One ---", result, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        galaxies, empty_rows, empty_columns = [], [], []
        for i, x in enumerate(lines):
            if len(x) == x.count('.'):
                empty_rows.append(i)

            for j, y in enumerate(x):
                if y == '#':
                    galaxies.append((i, j))

        lines_transposed = list(zip(*lines))
        for i, x in enumerate(lines_transposed):
            if len(x) == x.count('.'):
                empty_columns.append(i)

        result = sum(map(
            lambda p: \
                abs(p[0][0]-p[1][0]) + \
                abs(p[0][1]-p[1][1]) + \
                999999*sum(1 for x in empty_rows if (x > min(p[0][0], p[1][0])) and (x < max(p[0][0], p[1][0]))) + \
                999999*sum(1 for y in empty_columns if (y > min(p[0][1], p[1][1])) and (y < max(p[0][1], p[1][1]))),
            itertools.combinations(galaxies, 2)))

    print("--- Part Two ---", result, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
