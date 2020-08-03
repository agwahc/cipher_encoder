def update(a):  # updates work1.txt with words not present in db
    f = open('work1.txt', 'a')
    f.write(' ')
    f.write(a)
    f.close()
    return None
