from cipherz import iterate
from cipherz import recover
from cipherz import encoder
import rand_gen
import server as sv


def clear_rand_tmp():  # used to clean rand_tmp.txt after each use
    j = open('rand_tmp.txt', 'r+')
    k = open('fill_tmp.txt', 'r+')
    j.truncate(0)  # works perfectly
    k.truncate(0)
    j.close()
    k.close()
    repopulate_rand_tmp()


def repopulate_rand_tmp():
    rand_gen.sorter()
    start()


def start():
    encoder.data()
    send()


def send():
    sv.transfer()
    print('Finished process')


if __name__ == '__main__':
    clear_rand_tmp()
