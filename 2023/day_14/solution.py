from functools import cache

def roll_north(lines):
    max_rows = len(lines)
    max_cols = len(lines[0])
    rolls = 1
    while rolls > 0:
        rolls = 0
        for i in range(max_rows):
            for j in range(max_cols):
                if lines[i][j] == 'O' and i-1 >= 0 and lines[i-1][j] == '.':
                    lines[i][j] = '.'
                    lines[i-1][j] = 'O'
                    rolls += 1

@cache
def roll_line(line, direction):
    line = list(line)
    line_len = len(line)

    if direction in ('north', 'west'):
        r = range(line_len-1, 0, -1)
        diff = -1
    elif direction in ('south', 'east'):
        r = range(line_len-1)
        diff = 1

    rolls = 1
    while rolls > 0:
        rolls = 0
        for i in r:
            if line[i] == 'O' and line[i+diff] == '.':
                line[i], line[i+diff] = '.', 'O'
                rolls += 1

    return ''.join(line)

@cache
def roll_platform(platform, direction):
    platform = platform.split(',')
    if direction in ('north', 'south'):
        platform = list(map(lambda x: ''.join(x), zip(*platform)))

    platform = list(map(lambda l: roll_line(l, direction), platform))

    if direction in ('north', 'south'):
        platform = list(map(lambda x: ''.join(x), zip(*platform)))

    return ','.join(platform)

@cache
def cycle_platform(platform):
    for direction in ('north', 'west', 'south', 'east'):
        platform = roll_platform(platform, direction)
    return platform

def get_total_load_north(lines):
    total_load = 0
    for weight, line in zip(range(len(lines), 0, -1), lines):
        total_load += weight * line.count('O')
    return total_load

def part_1():
    with open('input') as file:
        lines = list(map(list, file.read().splitlines()))
        roll_north(lines)
        total_load = get_total_load_north(lines)

    print("--- Part One ---", total_load, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        platform = ','.join(lines)

        for _ in range(1000000000):
            platform = cycle_platform(platform)

        total_load = get_total_load_north(platform.split(','))

    print("--- Part Two ---", total_load, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
