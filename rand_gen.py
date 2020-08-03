import random


def sorter():  # used to randomly shuffle word placement in work1.txt
    g = open('work1.txt', 'r')
    j = open('rand_tmp.txt', 'a')
    b = []
    for i in g:
        x = i.split()
    random.shuffle(x)
    # shuffled x is still a list so we use lister() to convert to single extended line for rand_tmp.txt
    for q in x:
        b.append(q)
    for a in b:
        j.write(a)  # worked like a charm
        j.write(' ')
    g.close()
    j.close()
    return None
