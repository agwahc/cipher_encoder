def iterate(n, h):  # find word in rand_tmp.txt and return preceding word
    f = open('fill_tmp.txt', 'a')
    b = []
    for i in n:
        for o in h:
            if i == o:
                # print('Found!')
                v = h.index(o) - 1
                j = (h[v])
                b.append(j)
                break
        else:
            import learn
            learn.update(i)
            b.append(i)

        # Build encoded message using index-sourced data

    for a in b:
        f.write(a)  # worked like a charm
        f.write(' ')
    f.write('\n')
    f.close()
    return None
