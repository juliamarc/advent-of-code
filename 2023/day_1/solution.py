import re

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()

    sum_all = 0
    for line in lines:
        matches = re.findall(r'\d', line)
        first_digit = matches[0]
        last_digit = matches[-1]
        sum_all += int(first_digit + last_digit)

    print("--- Part One ---", sum_all, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()

    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    sum_all = 0
    for line in lines:
        matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        results = [match.group(1) for match in matches]
        first_digit = digit_map.get(results[0], results[0])
        last_digit = digit_map.get(results[-1], results[-1])
        sum_all += int(first_digit + last_digit)

    print("--- Part Two ---", sum_all, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
