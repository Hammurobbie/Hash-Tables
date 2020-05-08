import operator

# Implement me.
words = open("applications/histo/robin.txt").read()


def histo_boi(words):

    cache = {}

    # byePunc = s.translate(str.maketrans('', '', string.punctuation))
    byePunc = words.translate(str.maketrans(
        '":;,.-+=/\\|[]{}()*^&', '                    '))
    toLower = byePunc.lower()
    split = toLower.split()
    for i in split:
        if i in cache:
            cache[i] += 1
        else:
            cache[i] = 1
    sorted_words = sorted(
        cache.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in sorted_words:
        print(f'{key}'.ljust(18) + f'{"#" * int(value)}')


histo_boi(words)
