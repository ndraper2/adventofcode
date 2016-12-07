def lights(instructions):
    grid = [['off' for i in range(1000)] for j in range(1000)]
    for instruction in instructions:
        if instruction.startswith('turn on'):
            parts = instruction.split(' ')
            x1, y1 = parts[2].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[4].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 'on'
        elif instruction.startswith('turn off'):
            parts = instruction.split(' ')
            x1, y1 = parts[2].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[4].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 'off'
        elif instruction.startswith('toggle'):
            parts = instruction.split(' ')
            x1, y1 = parts[1].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[3].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if grid[i][j] == 'on':
                        grid[i][j] = 'off'
                    elif grid[i][j] == 'off':
                        grid[i][j] = 'on'
    count = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] == 'on':
                count += 1
    return count


def brightness(instructions):
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for instruction in instructions:
        if instruction.startswith('turn on'):
            parts = instruction.split(' ')
            x1, y1 = parts[2].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[4].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] += 1
        elif instruction.startswith('turn off'):
            parts = instruction.split(' ')
            x1, y1 = parts[2].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[4].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = max(grid[i][j] - 1, 0)
        elif instruction.startswith('toggle'):
            parts = instruction.split(' ')
            x1, y1 = parts[1].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = parts[3].split(',')
            x2, y2 = int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] += 2
    brightness = 0
    for i in range(1000):
        for j in range(1000):
            brightness += grid[i][j]
    return brightness


if __name__ == '__main__':
    with open('input-6.txt', 'r') as f:
        instructions = f.read().splitlines()
    print(lights(instructions))
    print(brightness(instructions))
