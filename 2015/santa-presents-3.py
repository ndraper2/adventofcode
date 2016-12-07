def houses(directions):
    coordinates = [0, 0]
    houses = set()
    houses.add((0, 0))
    for direction in directions:
        if direction == '>':
            coordinates[0] += 1
        elif direction == '<':
            coordinates[0] -= 1
        elif direction == '^':
            coordinates[1] += 1
        elif direction == 'v':
            coordinates[1] -= 1
        houses.add((coordinates[0], coordinates[1]))
    print(coordinates)
    return len(houses)


def robo_houses(directions):
    santa_coordinates = [0, 0]
    robo_coordinates = [0, 0]
    houses = set()
    houses.add((0, 0))
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            move(direction, santa_coordinates, houses)
        else:
            move(direction, robo_coordinates, houses)
    print(santa_coordinates, robo_coordinates)
    return len(houses)


def move(direction, coordinates, houses):
        if direction == '>':
            coordinates[0] += 1
        elif direction == '<':
            coordinates[0] -= 1
        elif direction == '^':
            coordinates[1] += 1
        elif direction == 'v':
            coordinates[1] -= 1
        houses.add((coordinates[0], coordinates[1]))


if __name__ == '__main__':
    with open('input-3.txt', 'r') as f:
        directions = f.read()
    print(houses(directions))
    print(robo_houses(directions))
