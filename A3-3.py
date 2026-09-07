# 封装两个函数：
# load_expenses(path) 返回记录列表
# sum_by(records, key_name) 按任意列分组求和，并调用按员工求和

import csv
from pathlib import Path

def load_expenses(path) -> list:
    with open(path, 'r') as f:
        return list(csv.reader(f))

def sum_by(records, key_name) -> dict:
    result = {}
    title = records[0]
    try:
        key_no = title.index(key_name)
    except IndexError:
        print(f"{key_name}不存在")
        return result

    for record in records[1:]:
        tmp_key = record[key_no]
        tmp_value = float(record[4])
        if tmp_key in result.keys():
            result[tmp_key] += tmp_value
        else:
            result[tmp_key] = tmp_value

    return result

source_path = Path(__file__).parent/'practice_data/expenses.csv'
print(sum_by(load_expenses(source_path),'员工'))