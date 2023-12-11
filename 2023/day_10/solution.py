import re

from collections import defaultdict

def find_start_pipe(all_pipes):
    for pipe_location, pipe_info in all_pipes.items():
        if pipe_info['pipe_type'] == 'S':
            return pipe_location

def pipes_to_neighbors(all_pipes):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    opposite_directions = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left'
    }
    pipe_directions = {
        'S': ['up', 'down', 'left', 'right'],
        '|': ['up', 'down'],
        '-': ['left', 'right'],
        'L': ['up', 'right'],
        'J': ['up', 'left'],
        '7': ['down', 'left'],
        'F': ['down', 'right']
    }
    for pipe_location, pipe_info in all_pipes.items():
        all_pipes[pipe_location]['neighbors'] = []
        pipe_type = pipe_info['pipe_type']
        pipe_direction = pipe_directions[pipe_type]

        for d in map(lambda x: directions[x], pipe_direction):
            potential_neighbor = (pipe_location[0] + d[0], pipe_location[1] + d[1])
            neighbor_exists = potential_neighbor in all_pipes

            if not neighbor_exists:
                continue

            neighbor_pipe_type = all_pipes[potential_neighbor]['pipe_type']
            neighbor_pipe_direction = pipe_directions[neighbor_pipe_type]
            opposite_neighbor_pipe_direction = list(map(lambda x: opposite_directions[x], neighbor_pipe_direction))

            if set.intersection(
                    set(opposite_neighbor_pipe_direction),
                    set(pipe_direction)):
                all_pipes[pipe_location]['neighbors'].append(potential_neighbor)

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]['neighbors']:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

def part_1():
    with open('input') as file:
        lines = file.read().splitlines()
        all_pipes = defaultdict(dict)
        for i, x in enumerate(lines):
            for j, y in enumerate(x):
                if y in list('S|-LJ7F'):
                    all_pipes[(i, j)]['pipe_type'] = y

        pipes_to_neighbors(all_pipes)
        start_pipe = find_start_pipe(all_pipes)
        cycles = [[start_pipe]+path for path in dfs(all_pipes, start_pipe, start_pipe)]

    print("--- Part One ---", ((max(map(len, cycles)))-1)/2, sep='\n')

def part_2():
    with open('input') as file:
        lines = file.read().splitlines()
        all_pipes = defaultdict(dict)
        for i, x in enumerate(lines):
            for j, y in enumerate(x):
                if y in list('S|-LJ7F'):
                    all_pipes[(i, j)]['pipe_type'] = y

        pipes_to_neighbors(all_pipes)
        start_pipe = find_start_pipe(all_pipes)
        cycles = [[start_pipe]+path for path in dfs(all_pipes, start_pipe, start_pipe)]
        cycles.sort(key=lambda x: len(x), reverse=True)
        loop = cycles[0][:-1]

        tiles_in_loop_count = 0
        max_rows = len(lines)
        max_columns = len(lines[0])
        lines = list(map(list, lines))
        for x, y in [(x, y) for x in range(max_rows) for y in range(max_columns)]:
            if lines[x][y] != '.' and (x, y) not in loop:
                lines[x][y] = 'X'
        for x, y in [(x, y) for x in range(max_rows) for y in range(max_columns)]:
            if (x, y) in loop:
                continue
            else:
                left, right = ''.join(lines[x][:y]), ''.join(lines[x][y+1:])
                col = list(map(lambda l: l[y], lines))
                above, below = ''.join(col[:x]), ''.join(col[x+1:])
                horizontal_pattern = r'\|{1}|F\-*J|L\-*7'
                vertical_pattern = r'\-{1}|7\|*L|F\|*J'
                left_cnt, right_cnt = len(re.findall(horizontal_pattern, left)), len(re.findall(horizontal_pattern, right))
                above_cnt, below_cnt = len(re.findall(vertical_pattern, above)), len(re.findall(vertical_pattern, below))
                if (left_cnt % 2 == 1) and (right_cnt % 2 == 1) and (above_cnt % 2 == 1) and (below_cnt % 2 == 1):
                    tiles_in_loop_count += 1
                    lines[x][y] = 'I'
                else:
                    lines[x][y] = 'O'

        print(*lines, sep='\n')

    print("--- Part Two ---", tiles_in_loop_count, sep='\n')


if __name__ == "__main__":
    part_1()
    part_2()
