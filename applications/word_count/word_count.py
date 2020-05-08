import string


def word_count(s):
    cache = {}
    # byePunc = s.translate(str.maketrans('', '', string.punctuation))
    byePunc = s.translate(str.maketrans(
        '":;,.-+=/\\|[]{}()*^&', '                    '))
    toLower = byePunc.lower()
    split = toLower.split()
    for i in split:
        if i in cache:
            cache[i] += 1
        else:
            cache[i] = 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
