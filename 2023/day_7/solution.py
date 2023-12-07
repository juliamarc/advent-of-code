import re
from collections import Counter
from functools import cmp_to_key

def compare_hands(h1, h2):
    h1, h2 = h1[0], h2[0]
    card_strength = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    hand_strength = {
        (1, 1, 1, 1, 1): 2,
        (2, 1, 1, 1): 3,
        (2, 2, 1): 4,
        (3, 1, 1): 5,
        (3, 2): 6,
        (4, 1): 7,
        (5,): 8
    }
    h1_cnt = tuple(sorted(list(Counter(h1).values()), reverse=True))
    h2_cnt = tuple(sorted(list(Counter(h2).values()), reverse=True))
    h1_strength = hand_strength[h1_cnt]
    h2_strength = hand_strength[h2_cnt]

    if h1_strength == h2_strength:
        h1_card_strengths = map(lambda x: card_strength[x], h1)
        h2_card_strengths = map(lambda x: card_strength[x], h2)
        for h1_card_strength, h2_card_strength in zip(h1_card_strengths, h2_card_strengths):
            if h1_card_strength != h2_card_strength:
                return h1_card_strength - h2_card_strength

    return h1_strength - h2_strength

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        hands = list(map(lambda x: tuple(x.split(' ')), lines))
        hands.sort(key=cmp_to_key(compare_hands))
        winnings = map(lambda x: x[0]*int(x[1][1]), enumerate(hands, start=1))

    print("--- Part One ---", sum(winnings), sep='\n')

def compare_joker_hands(h1, h2):
    h1, h2 = h1[0], h2[0]
    card_strength = {
        'J': 1,
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10, 'Q': 12, 'K': 13, 'A': 14
    }
    hand_strength = {
        (1, 1, 1, 1, 1): 2,
        (2, 1, 1, 1): 3,
        (2, 2, 1): 4,
        (3, 1, 1): 5,
        (3, 2): 6,
        (4, 1): 7,
        (5,): 8
    }
    h1_cnt = Counter(h1)
    h1_joker_cnt = h1_cnt.pop('J') if 'J' in h1_cnt and len(h1_cnt) > 1 else 0
    h1_cnt = sorted(list(h1_cnt.values()), reverse=True)
    h1_cnt[0] += h1_joker_cnt
    h1_cnt = tuple(h1_cnt)

    h2_cnt = Counter(h2)
    h2_joker_cnt = h2_cnt.pop('J')  if 'J' in h2_cnt and len(h2_cnt) > 1 else 0
    h2_cnt = sorted(list(h2_cnt.values()), reverse=True)
    h2_cnt[0] += h2_joker_cnt
    h2_cnt = tuple(h2_cnt)

    h1_strength = hand_strength[h1_cnt]
    h2_strength = hand_strength[h2_cnt]

    if h1_strength == h2_strength:
        h1_card_strengths = map(lambda x: card_strength[x], h1)
        h2_card_strengths = map(lambda x: card_strength[x], h2)
        for h1_card_strength, h2_card_strength in zip(h1_card_strengths, h2_card_strengths):
            if h1_card_strength != h2_card_strength:
                return h1_card_strength - h2_card_strength

    return h1_strength - h2_strength

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        hands = list(map(lambda x: tuple(x.split(' ')), lines))
        hands.sort(key=cmp_to_key(compare_joker_hands))
        winnings = map(lambda x: x[0]*int(x[1][1]), enumerate(hands, start=1))

    print("--- Part Two ---", sum(winnings), sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
