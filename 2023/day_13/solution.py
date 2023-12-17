from Levenshtein import distance

def find_adjacent_duplicates(pattern):
    duplicates = []
    for i in range(len(pattern) - 2 + 1):
        p = pattern[i: i + 2]
        p1, p2 = p[0], p[1]
        if p1 == p2:
            duplicates.append((i, i+1))
    return duplicates

def verify_duplicates(pattern, duplicates):
    p = len(pattern)
    for dx, dy in duplicates:
        reflection_len = min(dx+1, p-dy)
        left = pattern[dx-reflection_len+1:dx+1]
        right = pattern[dy:dy+reflection_len]
        right.reverse()
        if left == right:
            return (dx, dy)

def find_smudge_candidates(pattern):
    candidates = []
    for i in range(len(pattern)):
        for j in range(i, len(pattern)):
            if i != j:
                ld = distance(pattern[i], pattern[j])
                if ld == 1:
                    candidates.append((i, j))
    return candidates

def part_1():
    with open('input') as file:
        patterns = list(map(lambda x: x.splitlines(), file.read().split('\n\n')))
        patterns_cnt = len(patterns)
        patterns_transposed = list(map(
            lambda x: list(map(
                lambda y: ''.join(y),
                list(zip(*x)))),
            patterns))
        patterns.extend(patterns_transposed)

        s = 0
        for i, pattern in enumerate(patterns):
            duplicates = find_adjacent_duplicates(pattern)
            mirror_location = verify_duplicates(pattern, duplicates)
            if mirror_location and i >= patterns_cnt:
                s += mirror_location[1]
            elif mirror_location and i < patterns_cnt:
                s += mirror_location[1]*100

    print("--- Part One ---", s, sep='\n')

def part_2():
    with open('input') as file:
        patterns = list(map(lambda x: x.splitlines(), file.read().split('\n\n')))
        patterns_cnt = len(patterns)
        patterns_transposed = list(map(
            lambda x: list(map(
                lambda y: ''.join(y),
                list(zip(*x)))),
            patterns))
        patterns.extend(patterns_transposed)

        s = 0
        for i, pattern in enumerate(patterns):
            duplicates = find_adjacent_duplicates(pattern)
            original_mirror_location = verify_duplicates(pattern, duplicates)
            candidates = find_smudge_candidates(pattern)

            smudged_mirror_locations = []
            for c in candidates:
                p1, p2 = list(map(str, pattern)), list(map(str, pattern))
                p1[c[0]], p2[c[1]] = pattern[c[1]], pattern[c[0]]

                duplicates_p1 = find_adjacent_duplicates(p1)
                if original_mirror_location in duplicates_p1:
                    duplicates_p1.remove(original_mirror_location)
                mirror_location_p1 = verify_duplicates(p1, duplicates_p1)
                duplicates_p2 = find_adjacent_duplicates(p2)
                if original_mirror_location in duplicates_p2:
                    duplicates_p2.remove(original_mirror_location)
                mirror_location_p2 = verify_duplicates(p2, duplicates_p2)

                smudged_mirror_locations.extend([mirror_location_p1, mirror_location_p2])

            smudged_mirror_location = next((item for item in smudged_mirror_locations if item is not None), None)
            if smudged_mirror_location and i >= patterns_cnt:
                s += smudged_mirror_location[1]
            elif smudged_mirror_location and i < patterns_cnt:
                s += smudged_mirror_location[1]*100

    print("--- Part Two ---", s, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
