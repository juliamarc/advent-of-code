import re

def get_diffs(l):
    return [j-i for i, j in list(zip(l[:-1], l[1:]))]

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        seqs = list(map(lambda l: list(map(int, re.findall(r'-?\d+', l))), lines))

        sum_extra = 0
        for s in seqs:
            diffs = [s + [0]]
            while not all([e == 0 for e in s]):
                s = get_diffs(s)
                diffs.append(s + [0])

            for i in range(len(diffs)-1, -1, -1):
                diffs[i][-1] = diffs[i][-2] + diffs[i+1][-1] if i+1 < len(diffs) else 0

            sum_extra += diffs[0][-1]

    print("--- Part One ---", sum_extra, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        seqs = list(map(lambda l: list(map(int, re.findall(r'-?\d+', l))), lines))

        sum_extra = 0
        for s in seqs:
            diffs = [[0] + s]
            while not all([e == 0 for e in s]):
                s = get_diffs(s)
                diffs.append([0] + s)

            for i in range(len(diffs)-1, -1, -1):
                diffs[i][0] = diffs[i][1] - diffs[i+1][0] if i+1 < len(diffs) else 0

            sum_extra += diffs[0][0]

    print("--- Part Two ---", sum_extra, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
