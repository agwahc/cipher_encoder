from cipherz import iterate
from cipherz import recover
from cipherz import encoder
import rand_gen


def clear_rand_tmp():  # used to clean rand_tmp.txt after each use
    j = open('rand_tmp.txt', 'r+')
    j.truncate(0)  # works perfectly
    j.close()
    repopulate_rand_tmp()


def repopulate_rand_tmp():
    rand_gen.sorter()
    start()


def start():
    encoder.data()


if __name__ == '__main__':
    clear_rand_tmp()
