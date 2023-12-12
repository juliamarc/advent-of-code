import math
import re
import itertools

def part_1():
    with open('input_example') as file:
        lines = list(map(
            lambda r: (
                r[0],
                list(map(int, re.findall(r'\d+', r[1])))),
            map(lambda l: l.split(' '), file.read().splitlines())))

    sum_valid_combs = 0
    for l in lines:
        original_record = l[0]
        known_broken_cnt = original_record.count('#')
        expected_broken_cnt = sum(l[1])
        missing_broken_cnt = expected_broken_cnt - known_broken_cnt
        unknown_idx = [m.start() for m in re.finditer(r'\?', original_record)]
        all_combs = list(itertools.combinations(unknown_idx, missing_broken_cnt))
        valid_combs = 0
        for comb in all_combs:
            original_record_copy = list(original_record)
            for i in range(len(original_record_copy)):
                if i in comb:
                    original_record_copy[i] = '#'
                elif original_record_copy[i] == '?':
                    original_record_copy[i] = '.'
            original_record_copy = ''.join(original_record_copy)

            comb_broken_cnt = list(map(len, re.findall(r'#+', original_record_copy)))
            if comb_broken_cnt == l[1]:
                valid_combs += 1

        sum_valid_combs += valid_combs

    print("--- Part One ---", sum_valid_combs, sep='\n')

def part_2():
    with open('input_example') as file:
        lines = list(map(
            lambda r: (
                '?'.join([r[0]]*5),
                list(map(int, re.findall(r'\d+', r[1])))*5),
            map(lambda l: l.split(' '), file.read().splitlines())))
    
    sum_valid_combs = 0
    for l in lines:
        original_record = l[0]
        known_broken_cnt = original_record.count('#')
        expected_broken_cnt = sum(l[1])
        missing_broken_cnt = expected_broken_cnt - known_broken_cnt
        unknown_idx = [m.start() for m in re.finditer(r'\?', original_record)]
        all_combs = list(itertools.combinations(unknown_idx, missing_broken_cnt))
        valid_combs = 0
        for comb in all_combs:
            original_record_copy = list(original_record)
            for i in range(len(original_record_copy)):
                if i in comb:
                    original_record_copy[i] = '#'
                elif original_record_copy[i] == '?':
                    original_record_copy[i] = '.'
            original_record_copy = ''.join(original_record_copy)

            comb_broken_cnt = list(map(len, re.findall(r'#+', original_record_copy)))
            if comb_broken_cnt == l[1]:
                valid_combs += 1

        sum_valid_combs += valid_combs
        
        # print(*list(lines), sep='\n')

    print("--- Part Two ---", sum_valid_combs, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
