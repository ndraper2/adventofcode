import regex as re


def support_tls(ips):
    count = 0
    for ip in ips:
        abba = re.findall(r'([a-z])([a-z])\2\1', ip)
        bracket_abba = re.findall(r'\[[a-z]*?([a-z])([a-z])\2\1[a-z]*?\]', ip)
        abba_okay = False
        bracket_okay = True

        if abba:
            abba_okay = True
            for match in abba:
                if match[0] == match[1]:
                    abba_okay = False
                else:
                    abba_okay = True
                    break

        if bracket_abba:
            bracket_okay = False
            for match in bracket_abba:
                if match[0] == match[1]:
                    bracket_okay = True
                else:
                    bracket_okay = False
                    break

        if abba_okay and bracket_okay:
            count += 1
    return count


def support_ssl(ips):
    count = 0
    for i, ip in enumerate(ips):
        aba = re.findall(r'(?<!\[[a-z]*?)([a-z])([a-z])\1(?![a-z]*?\])', ip, overlapped=True)
        bab = re.findall(r'(?<=\[[a-z]*?)([a-z])([a-z])\1(?=[a-z]*?\])', ip, overlapped=True)
        for match in aba:
            if match[0] != match[1] and (match[1], match[0]) in bab:
                count += 1
                break
    return count


if __name__ == '__main__':
    with open('input7-1.txt', 'r') as f:
        ips = f.read().splitlines()
    print(support_tls(ips))
    print(support_ssl(ips))
