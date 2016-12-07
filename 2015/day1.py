def elevator(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
    return floor


def basement(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        if floor < 0:
            return i


if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        instructions = f.read().splitlines()
    print(elevator(instructions[0]))
    print(basement(instructions[0]))
