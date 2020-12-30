import threading

import time

d = {}

def create(key, value, timeout=0):
    if key in d:
        print('This key already exists')
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    d[key]=l
            else:
                print('Meory limit exceeded')
        else:
            print('Invalid key name')

def read(key):
    if key not in d:
        print('This key is not exist in database')
    else:
        b = d[key]
        if b[1]!= 0:
            if time.time()<b[1]:
                stri = str(key)+":"+str(b[0])
                return stri
            else:
                print('Given time interval of', key, 'has expired')
        else:
            stri = str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in d:
        print('Given key does not exist in database')
    else:
        b = d[key]
        if b[1] != 0:
            if time.time()<b[1]:
                del d[key]
                print('Key is successfully deleted')
            else:
                print('Given time interval of', key, 'has expired')
        else:
            del d[key]
            print('Key is successfully deleted')
