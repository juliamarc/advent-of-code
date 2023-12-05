import re

def flatten(l):
    if l in ([],()):
        return l

    if isinstance(l[0], (list, tuple)):
        l[0] = list(l[0])
        return flatten(l[0]) + flatten(l[1:])

    return l[:1] + flatten(l[1:])

def get_range_overlap(x, y):
    overlap = (max(x[0], y[0]), min(x[1], y[1]))
    remaining_left = (min(x[0], y[0]), max(x[0], y[0]))
    remaining_right = (min(x[1], y[1]), max(x[1], y[1]))

    if (overlap[0] != overlap[1]) and (overlap[0] < overlap[1]):
        if (remaining_left[0] == remaining_left[1]) or (remaining_left[1] != overlap[0]):
            remaining_left =  None
        if (remaining_right[0] == remaining_right[1]) or (remaining_right[0] != overlap[1]):
            remaining_right =  None
    else:
        overlap = None
        remaining_left = None
        remaining_right = None

    return overlap, remaining_left, remaining_right

def find_location(maps, source_type, source_value):
    if source_type == 'location':
        return source_value
    destination_type = maps[source_type]['destination_type']

    if isinstance(source_value, int):
        for mapping in maps[source_type]['mapping']:
            source_mapping_interval = (mapping['source'], mapping['source'] + mapping['range'])
            if (source_value >= source_mapping_interval[0]) and (source_value < source_mapping_interval[1]):
                destination_value = source_value - (mapping['source'] - mapping['destination'])
                break
        else:
            destination_value = source_value

        return find_location(maps, destination_type, destination_value)

    elif isinstance(source_value, tuple):
        if source_value[1] - source_value[0] == 1:
            return find_location(maps, source_type, source_value[0])

        source_interval = source_value
        locations = []

        for mapping in maps[source_type]['mapping']:
            source_mapping_interval = (mapping['source'], mapping['source'] + mapping['range'])
            overlap, remaining_left, remaining_right = get_range_overlap(source_interval, source_mapping_interval)

            if overlap:
                destination_value = (
                    overlap[0] +  - (mapping['source'] - mapping['destination']),
                    overlap[1] +  - (mapping['source'] - mapping['destination']))

                locations.append(
                    find_location(maps, destination_type, destination_value))
                if remaining_left is not None and (remaining_left[0] == source_interval[0]):
                    locations.append(
                        find_location(maps, source_type, remaining_left))
                if remaining_right is not None and (remaining_right[1] == source_interval[1]):
                    locations.append(
                        find_location(maps, source_type, remaining_right))
                break
        else:
            locations.append(
                find_location(maps, destination_type, source_interval))
        return locations

def part_1():
    with open('input') as file:
        maps_raw = re.split(r'\n\n', file.read())
        seeds = list(map(int, re.findall(r'(\d+)', maps_raw[0])))
        maps = {}
        for m in maps_raw[1:]:
            m = m.split('\n')
            source_type, destination_type = re.findall(r'(\w+)-to-(\w+)\s+map:', m[0])[0]
            value = {'destination_type': destination_type}
            value['mapping'] = list(map(
                lambda y: {'source': y[1], 'destination': y[0], 'range': y[2]},
                map(
                    lambda z: [int(w) for w in z],
                    map(lambda x: re.findall(r'\d+', x), m[1:]))))
            maps[source_type] = value

        locations = list(map(lambda s: find_location(maps, 'seed', s), seeds))

    print("--- Part One ---", min(locations), sep='\n')

def part_2():
    with open('input') as file:
        maps_raw = re.split(r'\n\n', file.read())
        seeds = list(map(int, re.findall(r'(\d+)', maps_raw[0])))
        seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
        seeds = list(map(lambda s: (s[0], s[0]+s[1]), seeds))
        maps = {}
        for m in maps_raw[1:]:
            m = m.split('\n')
            source_type, destination_type = re.findall(r'(\w+)-to-(\w+)\s+map:', m[0])[0]
            value = {'destination_type': destination_type}
            value['mapping'] = list(map(
                lambda y: {'source': y[1], 'destination': y[0], 'range': y[2]},
                map(
                    lambda z: [int(w) for w in z],
                    map(lambda x: re.findall(r'\d+', x), m[1:]))))
            maps[source_type] = value

        locations = list(map(lambda s: find_location(maps, 'seed', s), seeds))

    print("--- Part Two ---", min(flatten(locations)), sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
