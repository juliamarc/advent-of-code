import re

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()

    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    sum_possible_games = 0
    for line in lines:
        line_split = re.split(':', line)
        game_number = int(re.match(r'Game\s+(\d+)', line_split[0]).group(1))
        color_draws = re.findall(r'(\d+)\s+(red|green|blue)', line_split[1])
        for draw in color_draws:
            number = int(draw[0])
            color = draw[1]
            if number > bag[color]:
                break
        else:
            sum_possible_games += game_number

    print("--- Part One ---", sum_possible_games, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()

    sum_of_power = 0
    for line in lines:
        min_bag = {
            'red': None,
            'green': None,
            'blue': None
        }
        line_split = re.split(':', line)
        color_draws = re.findall(r'(\d+)\s+(red|green|blue)', line_split[1])

        for draw in color_draws:
            number = int(draw[0])
            color = draw[1]
            if min_bag[color] is None or number > min_bag[color]:
                min_bag[color] = number

        power = min_bag['red']*min_bag['green']*min_bag['blue']
        sum_of_power += power
        print(min_bag)

    print("--- Part Two ---", sum_of_power, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
