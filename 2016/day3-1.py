def triangles(instructions):
    count = 0
    for triangle in instructions:
        sides = triangle.split()
        for i, side in enumerate(sides):
            sides[i] = int(side)
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            count += 1
    return count


def columns(instructions):
    count = 0
    triangles = [[] for i in range(3)]
    for i, row in enumerate(instructions):
        sides = row.split()
        for j, side in enumerate(sides):
            triangles[j].append(int(side))
        if i % 3 == 2:
            for triangle in triangles:
                triangle.sort()
                if triangle[0] + triangle[1] > triangle[2]:
                    count += 1
            triangles = [[] for i in range(3)]
    return count


if __name__ == '__main__':
    with open('input3-1.txt', 'r') as f:
        instructions = f.read().splitlines()
    print(triangles(instructions))
    print(columns(instructions))
