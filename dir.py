import os

find = os.path.dirname(__file__)


def rand_tmp():
    return find + '/rand_tmp.txt'


def fill_tmp():
    return find + '/fill_tmp.txt'


def fill_tmp_png():
    return find + '/fill_tmp.png'
