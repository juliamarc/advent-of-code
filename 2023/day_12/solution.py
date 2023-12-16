import re

def matches(text, numbers):
    states = "."
    for nr in numbers:
        for i in range(int(nr)):
            states += "#"
        states += "."

    states_dict = {0: 1}
    new_dict = {}
    for char in text:
        for state in states_dict:
            if char == "?":
                if state + 1 < len(states):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == ".":
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == "#":
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]

        states_dict = new_dict
        new_dict = {}

    return states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)

def part_1():
    with open('input') as file:
        lines = list(map(
            lambda r: (
                r[0],
                list(map(int, re.findall(r'\d+', r[1])))),
            map(lambda l: l.split(' '), file.read().splitlines())))

    sum_valid_combs = sum(map(lambda l: matches(l[0], l[1]),lines))

    print("--- Part One ---", sum_valid_combs, sep='\n')

def part_2():
    with open('input') as file:
        lines = list(map(
            lambda r: (
                '?'.join([r[0]]*5),
                list(map(int, re.findall(r'\d+', r[1])))*5),
            map(lambda l: l.split(' '), file.read().splitlines())))

    sum_valid_combs = sum(map(lambda l: matches(l[0], l[1]),lines))

    print("--- Part Two ---", sum_valid_combs, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
