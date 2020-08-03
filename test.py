import random
''' #used to generate single word per line in work1.txt
def new_txt():
    f = open('work.txt', 'r')
    for i in f:
        x = i.split()
        n = open('work1.txt', 'a')
        for q in x:
            n.write(q)
            n.write('\n')
        n.close()
    f.close()


def lister(): #to make work1.txt a single extended line of words in work.txt
    f = open('work1.txt', 'r')
    g = open('work.txt', 'a')
    b = []
    for i in f:
        x = i.split()
        for q in x:
            b.append(q)
    for a in b:
        g.write(a) #worked like a charm
        g.write(' ')
    f.close()
    g.close()


def recover(): #To try to recover elements in list form list from work.txt
    g = open('work.txt', 'r')
    for i in g:
        x = i.split()
    print(x)


def sorter(): #used to randomly shuffle word placement in work1.txt
    #using code from def recover()
    g = open('work.txt', 'r')
    j = open('rand_tmp.txt', 'a')
    b =[]
    for i in g:
        x = i.split()
    print(x)
    random.shuffle(x)
    #shuffled x is still a list so we use lister() to convert to single extended line for rand_tmp.txt
    for q in x:
        b.append(q)
    for a in b:
        j.write(a)  # worked like a charm
        j.write(' ')
    g.close()
    j.close()

def clean(): #used to clean rand_tmp.txt after each use
    j = open('rand_tmp.txt', 'r+')
    j.truncate(0)  #works perfectly
    j.close()

def try_recover():
    from cipherz import recover
    t = recover.recover('rand_tmp')
    print(t)


class gray:
    def __init__(self, a, b):
        self.sum = a * b

    def access(self):
        print(self.sum)
'''

def scramble():
    j = open('work1.txt', 'r')
    f = open('temp.txt', 'a')
    b = []
    for i in j:
        try:
            g = i.split()
            b.append(g[0])
            b.append(g[2])
            b.append(g[4])
        except:
            g = i.split()
            b.append(g[0])
            #b.append(g[2])
            #b.append(g[4])
    for x in b:
        f.write(x)
        f.write(' ')
    f.close()
    j.close()

def lens():
    f = open('temp.txt', 'r')
    for i in f:
        v = i.split()
    print(v)
    x =len(v)
    print(x)
if True:
    lens()