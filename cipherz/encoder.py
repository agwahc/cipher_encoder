from cipherz import recover
from cipherz import iterate as it
import dir
from datetime import datetime
# This file will read inputted data, extract individual words from rand_tmp.txt, replace them with their preceding
# counterparts, and produce an encoded output.
msg = {'Date/time': ' ', 'Actual_msg': ' ', 'Encoded_msg': ' '}


def data():  # reads data *ignores punctuations and ints
    try:
        a = str.casefold(input('Enter delight here : '))
        x = a.split()
        # use recover module to get rand_tmp.txt as list
        access = dir.rand_tmp()
        t = recover.recover(access)
        it.iterate(x, t)
        g = open('Encoded_msg.txt', 'a')
        msg['Date/time'] = datetime.now().strftime('%d/%m/%Y %H:%M')
        msg['Actual_msg'] = a
        access1 = dir.fill_tmp()
        msg['Encoded_msg'] = open(access1, 'r').read()
        g.write(str(msg))
        g.write('\n')
        g.close()
        print('werewolf')
    except:
        print('Invalid entry!')
        data()
