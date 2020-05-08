def no_dups(s):
    # Implement me.
    cache = {}
    split = s.split()
    for i in split:
        if i in cache:
            pass
        else:
            cache[i] = i
    newStr = " "
    b = []
    for i in cache:
        b.append(cache[i])
    if cache:
        return newStr.join(b)
    else:
        return ""


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
