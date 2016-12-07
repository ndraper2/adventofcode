from collections import Counter
import string


def real_rooms(rooms):
    count = 0
    for room in rooms:
        tokens = room.split('-')
        letters = ''.join(tokens[:-1])
        c = Counter(letters)
        common_sorted = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        compare = ''.join([x[0] for x in common_sorted[:5]])
        if compare == tokens[-1][4:9]:
            count += int(tokens[-1][:3])
    return count


def check_room(room):
    tokens = room.split('-')
    letters = ''.join(tokens[:-1])
    c = Counter(letters)
    common_sorted = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    compare = ''.join([x[0] for x in common_sorted[:5]])
    if compare == tokens[-1][4:9]:
        return True


# http://stackoverflow.com/questions/26369035/caesar-cipher-issue/26371777#26371777
def shift(text, offset):
    alphabet = string.ascii_lowercase
    shifted = alphabet[offset:] + alphabet[:offset]
    return text.translate(text.maketrans(alphabet, shifted))


def north_pole(rooms):
    for room in rooms:
        # if check_room(room):
            tokens = room.split('-')
            name = ' '.join(tokens[:-1])
            number = int(tokens[-1][:3])
            real_name = shift(name, number % 26)
            if 'northpole' in real_name:
                return number


if __name__ == '__main__':
    with open('input4-1.txt', 'r') as f:
        rooms = f.read().splitlines()
    print(real_rooms(rooms))
    print(north_pole(rooms))
