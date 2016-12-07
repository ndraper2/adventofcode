def get_blocks(instructions):
    x = 0
    y = 0
    direction = 200
    steps = instructions.split(', ')
    for step in steps:
        if step[0] == 'R':
            direction += 1
        elif step[0] == 'L':
            direction -= 1
        if direction % 4 == 0:
            y += int(step[1:])
        elif direction % 4 == 1:
            x += int(step[1:])
        elif direction % 4 == 2:
            y -= int(step[1:])
        elif direction % 4 == 3:
            x -= int(step[1:])

    return abs(x) + abs(y)


def get_location(instructions):
    x = 0
    y = 0
    direction = 200
    location = set()
    location.add((x, y))
    steps = instructions.split(', ')
    for num, step in enumerate(steps):
        count = int(step[1:])
        if step[0] == 'R':
            direction += 1
        elif step[0] == 'L':
            direction -= 1
        if direction % 4 == 0:
            for i in range(1, count + 1):
                y += 1
                if (x, y) in location:
                    return abs(x) + abs(y)
                location.add((x, y))
        elif direction % 4 == 1:
            for i in range(1, count + 1):
                x += 1
                if (x, y) in location:
                    return abs(x) + abs(y)
                location.add((x, y))
        elif direction % 4 == 2:
            for i in range(1, count + 1):
                y -= 1
                if (x, y) in location:
                    return abs(x) + abs(y)
                location.add((x, y))
        elif direction % 4 == 3:
            for i in range(1, count + 1):
                x -= 1
                if (x, y) in location:
                    return abs(x) + abs(y)
                location.add((x, y))


if __name__ == '__main__':
    with open('input1-1.txt', 'r') as f:
        instructions = f.read()
    print(get_blocks(instructions))
    print(get_location(instructions))
