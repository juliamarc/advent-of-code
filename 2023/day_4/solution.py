import re

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        total_points = 0
        for line in lines:
            split_line = re.split(r':|\|', line)
            winning_numbers = re.findall(r'\d+', split_line[1])
            my_numbers = re.findall(r'\d+', split_line[2])
            matches = len(set(winning_numbers) & set(my_numbers))
            if matches == 1:
                total_points += 1
            elif matches > 1:
                total_points += 2**(matches-1)

    print("--- Part One ---", total_points, sep='\n')

def count_cards(cards_dict, cards_to_visit):
    for card in cards_to_visit:
        cards_dict[card]['count'] += 1
        card_matches = cards_dict[card]['matches']
        if card_matches > 0:
            count_cards(cards_dict, range(card+1, card+card_matches+1))

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        cards_dict = {}
        for line in lines:
            split_line = re.split(r':|\|', line)
            card_number = int(re.findall(r'\d+', split_line[0])[0])
            winning_numbers = re.findall(r'\d+', split_line[1])
            my_numbers = re.findall(r'\d+', split_line[2])
            matches = len(set(winning_numbers) & set(my_numbers))
            cards_dict[card_number] = {
                'matches': matches,
                'count': 0
            }
        count_cards(cards_dict, range(1, len(cards_dict)+1))
        total_cards = sum([v['count'] for v in cards_dict.values()])

    print("--- Part Two ---", total_cards, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
