import hashlib


def stocking_stuffers():
    i = 0
    while True:
        trial = 'bgvyzdsv' + str(i)
        m = hashlib.md5(trial)
        if m.hexdigest().startswith('00000'):
            print(i)
            break
        i += 1


def stocking_stuffers_2():
    i = 0
    while True:
        trial = 'bgvyzdsv' + str(i)
        m = hashlib.md5(trial)
        if m.hexdigest().startswith('000000'):
            print(i)
            break
        i += 1


if __name__ == '__main__':
    stocking_stuffers()
    stocking_stuffers_2()
