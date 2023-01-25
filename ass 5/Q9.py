a = input(str("enter a line : "))


def word_count(line):
    counts = dict()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count(a))
