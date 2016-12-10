from collections import Counter


def decode_repeater(messages):
    grid = [[] for i in range(len(messages[0]))]
    for message in messages:
        for i, letter in enumerate(message):
            grid[i].append(letter)
    decoded_message = []
    for column in grid:
        c = Counter(column)
        decoded_message.append(c.most_common(1)[0][0])
    return ''.join(decoded_message)


def decode_minimal(messages):
    grid = [[] for i in range(len(messages[0]))]
    for message in messages:
        for i, letter in enumerate(message):
            grid[i].append(letter)
    decoded_message = []
    for column in grid:
        c = Counter(column)
        decoded_message.append(c.most_common()[-1][0])
    return ''.join(decoded_message)


if __name__ == '__main__':
    with open('input6-1.txt', 'r') as f:
        messages = f.read().splitlines()
    print(decode_repeater(messages))
    print(decode_minimal(messages))
