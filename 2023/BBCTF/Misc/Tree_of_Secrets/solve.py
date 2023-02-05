#coding:utf-8

# import
import os
import glob
import base64

# fanc
def message_check(plist, msg):
    ccnt = 0
    for pl in plist:
        if pl[0] == msg:
            ccnt = ccnt + 1
    return ccnt
def get_message(plist, msg):
    for pl in plist:
        if pl[0] == msg:
            return pl[1]

# main
if __name__ == '__main__':

    path_list = []
    for g in glob.glob('./root/**', recursive=True):
        if os.path.isfile(g):
            buff = g[7:].split('/')
            path_list.append([''.join(buff[:-1]), buff[-1]])
    
    message = ''
    with open('./message', mode='r') as f:
        message = f.readline()

    flag = []
    idx = 0
    mlen = 0
    while len(message) != idx:
        if message_check(path_list, message[idx:idx+mlen]) == 1:
            flag.append(get_message(path_list, message[idx:idx+mlen]))
            idx = idx + mlen
            mlen = 0
        else:
            mlen = mlen + 1
    
    print(''.join(flag))
    print(base64.b64decode(''.join(flag)))
