def wrapping_paper(presents):
    paper = 0
    count = 0
    for present in presents:
        length, width, height = present.split('x')
        length, width, height = int(length), int(width), int(height)
        sides = (2 * length * width, 2 * width * height, 2 * height * length)
        smallest = min(sides) // 2
        present_paper = smallest
        for side in sides:
            present_paper += side
        paper += present_paper
        count += 1
    return paper, count


def ribbon(presents):
    ribbon = 0
    count = 0
    for present in presents:
        length, width, height = present.split('x')
        dimensions = sorted((int(length), int(width), int(height)))
        present_ribbon = dimensions[0] * 2 + dimensions[1] * 2
        # really, python? no product()?
        bow = dimensions[0] * dimensions[1] * dimensions[2]
        ribbon += (present_ribbon + bow)
        count += 1
    return ribbon, count


if __name__ == '__main__':
    with open('input-2.txt', 'r') as f:
        presents = f.read().splitlines()
    print(wrapping_paper(presents))
    print(ribbon(presents))
