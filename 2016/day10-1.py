from collections import defaultdict


def load_values(instructions):

    def activate_bot(bot):
        for instruction in instructions:
            if ' '.join(instruction.split(' ')[:2]) == bot:
                words = instruction.split(' ')
                low, high = sorted(bots[bot])
                lowtarget = ' '.join(words[5:7])
                hightarget = ' '.join(words[-2:])
                if low == 17 and high == 61:
                    print(bot)
                bots[lowtarget].append(low)
                if len(bots[lowtarget]) == 2:
                    activate_bot(lowtarget)
                bots[hightarget].append(high)
                if len(bots[hightarget]) == 2:
                    activate_bot(hightarget)
                break

    bots = defaultdict(list)
    for instruction in instructions:
        if instruction.startswith('value'):
            words = instruction.split(' ')
            target = ' '.join(words[-2:])
            bots[target].append(int(words[1]))
            if len(bots[target]) == 2:
                activate_bot(target)
    print(bots['output 0'][0] * bots['output 1'][0] * bots['output 2'][0])


if __name__ == '__main__':
    with open('input10-1.txt', 'r') as f:
        instructions = f.read().splitlines()
    load_values(instructions)
