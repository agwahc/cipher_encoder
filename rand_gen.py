import random
import pyqrcode


def sorter():  # used to randomly shuffle word placement in work1.txt
    g = open('db.txt', 'r')
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
    return None


'''
    x = ''
    for item in b:
        x = x + item + ' '
    qr = pyqrcode.create(x)
    qr.png('rand_tmp.png', scale=4)
    g.close()
    j.close()
'''

