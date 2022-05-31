import os
import csv
import datetime

filepath = "./co2data.csv"


def dict2csv(dict_permin: dict, lst_csv: list, deleteNum: int) -> list:
    lst = [datetime.datetime.now(), dict_permin["co2"]]
    lst_csv.append(lst)
    if len(lst_csv) > (deleteNum - 1):
        if os.path.isfile(filepath):
            with open(filepath, mode="a") as f:
                writer = csv.writer(f)
                writer.writerows(lst_csv)
        else:
            header = ["time", "co2"]
            with open(filepath, mode="w") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(lst_csv)
        lst_csv = []
    return lst_csv
