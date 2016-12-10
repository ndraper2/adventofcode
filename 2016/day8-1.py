def display_screen(instructions):
    grid = [[' ' for i in range(6)] for i in range(50)]
    for instruction in instructions:
        if instruction.startswith('rect'):
            x, y = instruction.split(' ')[-1].split('x')
            x, y = int(x), int(y)
            for i in range(x):
                for j in range(y):
                    grid[i][j] = 'X'
        elif instruction.startswith('rotate'):
            words = instruction.split(' ')
            shift = int(words[-1])
            axis, number = words[2].split('=')
            number = int(number)
            if axis == 'x':
                grid[number] = grid[number][-shift:] + grid[number][:-shift]
            elif axis == 'y':
                temprow = [grid[i][number] for i in range(50)]
                temprow = temprow[-shift:] + temprow[:-shift]
                for i in range(50):
                    grid[i][number] = temprow[i]
    count = 0
    for i in range(50):
        for j in range(6):
            if grid[i][j] == 'X':
                count +=1
    from pprint import pprint
    for item in grid:
        pprint(''.join(item))
    return count


if __name__ == '__main__':
    with open('input8-1.txt', 'r') as f:
        instructions = f.read().splitlines()
    print(display_screen(instructions))
    print('ruruceoeil')
