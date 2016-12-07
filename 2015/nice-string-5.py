import re


def nice_string(words):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    naughty = set(['ab', 'cd', 'pq', 'xy'])
    nice = 0
    count = 0
    for word in words:
        vowel_count = 0
        double_letter = False
        naughty_string = False
        letter = word[1]
        previous_letter = word[0]
        if previous_letter in vowels:
            vowel_count += 1
        for i in range(len(word) - 1):
            previous_letter = word[i]
            letter = word[i + 1]
            if letter in vowels:
                vowel_count += 1
            if letter == previous_letter:
                double_letter = True
            if previous_letter + letter in naughty:
                naughty_string = True
        if vowel_count >= 3 and double_letter and not naughty_string:
            nice += 1
        count += 1
    return nice, count


def new_rules(words):
    nice = 0
    for word in words:
        matches = re.findall(r'([a-z]{2})[a-z]*\1', word)
        matches_2 = re.findall(r'([a-z])[a-z]{1}\1', word)
        if matches and matches_2:
            nice += 1
    return nice


if __name__ == '__main__':
    with open('input-5.txt', 'r') as f:
        words = f.read().splitlines()
    print(nice_string(words))
    print(new_rules(words))
