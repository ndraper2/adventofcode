import hashlib


def get_password():
    puzzle = 'abbhdwsy'
    count = 0
    index = 0
    solution = ''
    while count < 8:
        test = hashlib.md5(puzzle + str(index)).hexdigest()
        if test.startswith('00000'):
            solution += test[5]
            count += 1
        index += 1
    return solution


def better_password():
    puzzle = 'abbhdwsy'
    index = 0
    solution = ['' for i in range(8)]
    while True:
        test = hashlib.md5(puzzle + str(index)).hexdigest()
        if test.startswith('00000'):
            try:
                position = int(test[5])
            except ValueError:
                index += 1
                continue
            if 0 <= position and position <= 7:
                if not solution[position]:
                    solution[position] = test[6]
                    mid = ''.join(solution)
                    print(mid)
                    if len(mid) == 8:
                        break
        index += 1
    return ''.join(solution)


if __name__ == '__main__':
    # print(get_password())
    print(better_password())
