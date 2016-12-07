def bathroom_code(instructions):
    key = {
        (0, 0): '1',
        (1, 0): '2',
        (2, 0): '3',
        (0, 1): '4',
        (1, 1): '5',
        (2, 1): '6',
        (0, 2): '7',
        (1, 2): '8',
        (2, 2): '9',
    }
    x = 1
    y = 1
    code = ''
    for instruction in instructions:
        for direction in instruction:
            if direction == 'U':
                y -= 1
                y = max(y, 0)
            elif direction == 'R':
                x += 1
                x = min(x, 2)
            elif direction == 'D':
                y += 1
                y = min(y, 2)
            elif direction == 'L':
                x -= 1
                x = max(x, 0)
        code += key[(x, y)]
    return code


def mean_code(instructions):
    key = {
        (0, 2): '1',
        (1, 1): '2',
        (2, 1): '3',
        (3, 1): '4',
        (0, 2): '5',
        (1, 2): '6',
        (2, 2): '7',
        (3, 2): '8',
        (4, 2): '9',
        (1, 3): 'A',
        (2, 3): 'B',
        (3, 3): 'C',
        (3, 4): 'D',
    }
    x = 0
    y = 2
    code = ''
    for instruction in instructions:
        for direction in instruction:
            if direction == 'U':
                y -= 1
                if x == 2:
                    y = max(y, 0)
                elif x == 1 or x == 3:
                    y = max(y, 1)
                elif x == 0 or x == 4:
                    y = 2
            elif direction == 'R':
                x += 1
                if y == 2:
                    x = min(x, 4)
                elif y == 1 or y == 3:
                    x = min(x, 3)
                elif y == 0 or y == 4:
                    x = 2
            elif direction == 'D':
                y += 1
                if x == 2:
                    y = min(y, 4)
                elif x == 1 or x == 3:
                    y = min(y, 3)
                elif x == 0 or x == 4:
                    y = 2
            elif direction == 'L':
                x -= 1
                if y == 2:
                    x = max(x, 0)
                elif y == 1 or y == 3:
                    x = max(x, 1)
                elif y == 0 or y == 4:
                    x = 2
        code += key[(x, y)]
    return code


if __name__ == '__main__':
    with open('input2-1.txt', 'r') as f:
        instructions = f.read().splitlines()
    print(bathroom_code(instructions))
    print(mean_code(instructions))
