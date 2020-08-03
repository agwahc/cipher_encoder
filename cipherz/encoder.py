from cipherz import recover
from cipherz import iterate as it
import dir


# This file will read inputted data, extract individual words from rand_tmp.txt, replace them with their preceding
# counterparts, and produce an encoded output.

def data():  # reads data *ignores punctuations and ints
    a = str.casefold(input('Enter delight here : '))
    x = a.split()
    # use recover module to get rand_tmp.txt as list
    access = dir.rand_tmp()
    t = recover.recover(access)
    it.iterate(x, t)
    print('werewolf')

