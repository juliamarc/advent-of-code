import re

def traverse_network(network, instructions):
    now, end, step_count = 'AAA', 'ZZZ', 0

    while now != end:
        now = network[now][instructions[step_count % len(instructions)]]
        step_count += 1

    return step_count

def part_1():
    with open('input') as file:
        data = file.read().split('\n\n')
        instructions = data[0]
        network = {
            x[0]: {'L': x[1], 'R': x[2]} for x in map(
                lambda y: re.findall(r'\w+', y), data[1].splitlines())}

    print("--- Part One ---", traverse_network(network, instructions), sep='\n')

def get_shortest_a2z_paths(network, instructions):
    now_list = [node for node in network.keys() if node.endswith('A')]
    a2z_paths = {}
    for now in now_list:
        step_count, path = 0, ''
        while not now.endswith('Z'):
            direction = instructions[step_count % len(instructions)]
            now = network[now][direction]
            path += direction
            step_count += 1

        a2z_paths[now] = path

    return a2z_paths

def nwd(a, b):
    x = 0
    while b != 0:
        x = a % b
        a, b = b, x
    return a

def nww(num_list):
    if len(num_list) == 2:
        return num_list[0]*num_list[1] // nwd(*num_list)
    else:
        return nww([num_list[0], nww(num_list[1:])])

def traverse_network_as_ghost(network, instructions):
    a2z_paths = get_shortest_a2z_paths(network, instructions)

    return nww([len(x) for x in a2z_paths.values()])

def part_2():
    with open('input') as file:
        data = file.read().split('\n\n')
        instructions = data[0]
        network = {
            x[0]: {'L': x[1], 'R': x[2]} for x in map(
                lambda y: re.findall(r'\w+', y), data[1].splitlines())}

    print("--- Part Two ---", traverse_network_as_ghost(network, instructions), sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
