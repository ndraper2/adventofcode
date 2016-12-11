def decompress(compressed):
    i = 0
    inflated = []
    while True:
        try:
            letter = compressed[i]
        except IndexError:
            break
        if letter == '(':
            marker = ''
            i += 1
            while compressed[i] != ')':
                marker += compressed[i]
                i += 1
            i += 1
            characters, repeat = marker.split('x')
            characters, repeat = int(characters), int(repeat)
            for j in range(repeat):
                inflated.append(compressed[i:i+characters])
            i += characters
        else:
            inflated.append(letter)
            i += 1
    inflated_string = ''.join(inflated)
    return len(inflated_string)


def version_two(compressed):
    i = 0
    count = 0
    while True:
        try:
            letter = compressed[i]
        except IndexError:
            break
        if letter == '(':
            marker = ''
            i += 1
            while compressed[i] != ')':
                marker += compressed[i]
                i += 1
            i += 1
            characters, repeat = marker.split('x')
            characters, repeat = int(characters), int(repeat)
            count += version_two(compressed[i:i+characters]) * repeat
            i += characters
        else:
            count += 1
            i += 1
    return count



if __name__ == '__main__':
    with open('input9-1.txt', 'r') as f:
        compressed = f.read().strip()
    print(decompress(compressed))
    print(version_two(compressed))
