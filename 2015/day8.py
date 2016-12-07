def count_string(inputs):
    literals = 0
    memory = 0
    for input_string in inputs:
        literals += len(input_string)
        memory -= 2
        slash = False
        for i, character in enumerate(input_string):
            if character == '\\':
                slash = not slash
                if slash:
                    if input_string[i+1] == '"':
                        slash = False
                        continue
                    elif input_string[i+1] == 'x':
                        slash = False
                        memory -= 2
                else:
                    memory += 1
            else:
                memory += 1
    print(literals, memory)
    return literals - memory


def encode_string(inputs):
    literals = 0
    encoded = 0
    for input_string in inputs:
        literals += len(input_string)
        new_string = 1
        for letter in input_string:
            if letter == '"':
                new_string += 2
            elif letter == '\\':
                new_string += 2
            else:
                new_string += 1
        new_string += 1
        encoded += new_string
    print(encoded, literals)
    return encoded - literals


if __name__ == '__main__':
    with open('input8.txt', 'r') as f:
        inputs = f.read().splitlines()
    print(count_string(inputs))
    print(encode_string(inputs))
