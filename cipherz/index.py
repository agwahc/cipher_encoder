import recover
import dir


def index():  # generate amd compare indexes
    o = recover.recover(dir.rand_tmp())
    a = []
    b = 0
    for i in o:
        a.append(b)
        b += 1

# Incomplete!