# -*- coding: utf-8 -*-
import time
import mh_z19

from save_csv import dict2csv

def schedule(interval, deleteNum):
    base_time = time.time()
    next_time = 0
    lst_csv = []
    while True:
        lst_csv = worker(lst_csv, deleteNum)
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)


def worker(lst_csv, deleteNum):
    value = mh_z19.read()
    print(value)
    lst_csv = dict2csv(value, lst_csv, deleteNum)
    return lst_csv

if __name__ == '__main__':
    schedule(60, 60)
