#coding:utf-8

# import
from string import ascii_lowercase, digits
from hashlib import md5

# fanction
def pos(alp, ch):
    return alphabets.find(ch)

# main
if __name__ == '__main__':

    alphabets = ascii_lowercase + digits + "_{}"

    c = 'oolivuidn4gkb}x98045u1io1yoz_z_jbp1l4f'

    for i in range(len(c)**4):
        f = ''
        flag = []
        key = [9, 3, 11, 2, 23, (i // (len(c)**3)) % len(c), (i // (len(c)**2)) % len(c), 6, (i // (len(c)**1)) % len(c), i % len(c)]
        for idx in range(len(c)):
            flag.append(alphabets[((len(alphabets) + pos(alphabets, c[idx])) - key[idx % 10]) % len(alphabets)])
        f = ''.join(flag)
        hs = md5(f.encode('ascii')).hexdigest()
        print(f, hs)