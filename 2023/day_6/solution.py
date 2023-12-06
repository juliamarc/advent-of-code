import re
from math import sqrt, ceil, floor

def get_delta(a, b, c):
    return b**2-4*a*c

def get_root(a, b, delta):
    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)
    return x1, x2

def get_integer_count_in_range(x, y):
    min_num = min(x, y)
    max_num = max(x, y)
    correction = 0
    if x.is_integer():
        correction -= 1
    if y.is_integer():
        correction -= 1
    return floor(max_num) + 1 - ceil(min_num) + correction

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        times = re.findall(r'\d+', lines[0])
        distances = re.findall(r'\d+', lines[1])
        races = list(zip(map(int, times), map(int, distances)))

        result = 1
        for r in races:
            a = -1
            b = r[0]
            c = -r[1]
            delta = get_delta(a, b, c)
            root = get_root(a, b, delta)
            cnt = get_integer_count_in_range(*root)
            result *= cnt

    print("--- Part One ---", result, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        time = int(''.join(re.findall(r'\d+', lines[0])))
        distance = int(''.join(re.findall(r'\d+', lines[1])))

        a = -1
        b = time
        c = -distance
        delta = get_delta(a, b, c)
        root = get_root(a, b, delta)
        result = get_integer_count_in_range(*root)

    print("--- Part Two ---", result, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
