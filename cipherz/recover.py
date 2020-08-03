def recover(source): #To try to recover elements in list structure from *source*.txt
    g = open('%s' %source, 'r')
    for i in g:
        n = str.casefold(i)
        x = n.split()
    return x