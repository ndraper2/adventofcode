import operator


def diagram(instructions):
    variables = {}

    def process_instruction(instruction):
        gate_input, gate_output = instruction.split('->')
        gate_input = gate_input.strip()
        gate_output = gate_output.strip()
        input_parts = gate_input.split(' ')
        if len(input_parts) == 2:
            variables[gate_output] = operator.inv(get_value(input_parts[1]))
        elif len(input_parts) == 1:
            try:
                first = int(input_parts[0])
            except ValueError:
                first = get_value(input_parts[0])
            variables[gate_output] = first
        else:
            if input_parts[1] == 'LSHIFT':
                variables[gate_output] = operator.lshift(get_value(input_parts[0]), int(input_parts[2]))
            elif input_parts[1] == 'RSHIFT':
                variables[gate_output] = operator.rshift(get_value(input_parts[0]), int(input_parts[2]))
            elif input_parts[1] == 'AND':
                try:
                    first = int(input_parts[0])
                except ValueError:
                    first = get_value(input_parts[0])
                variables[gate_output] = operator.and_(first, get_value(input_parts[2]))
            elif input_parts[1] == 'OR':
                try:
                    first = int(input_parts[0])
                except ValueError:
                    first = get_value(input_parts[0])
                variables[gate_output] = operator.or_(first, get_value(input_parts[2]))

    def get_value(node):
        try:
            return variables[node]
        except KeyError:
            for instruction in instructions:
                if instruction.split(' ')[-1] == node:
                    process_instruction(instruction)
                    break
            return variables[node]

    for instruction in instructions:
        process_instruction(instruction)

    return variables['a']


if __name__ == '__main__':
    with open('input-7.txt', 'r') as f:
        wiring = f.read().splitlines()
    print(diagram(wiring))
    with open('input-7-2.txt', 'r') as f:
        wiring = f.read().splitlines()
    print(diagram(wiring))
