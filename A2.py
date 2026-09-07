# 读取数据，用字典统计每个员工的报销总额
# 输出总额最高的三人（sorted()）
# 用字典统计每人每类费用

import csv
from pathlib import Path

source_path = Path(__file__).parent/'practice_data/expenses.csv'

try:
    with open(source_path, 'r') as f:
        data_list = list(csv.reader(f))[1:]
except FileNotFoundError:
    print(f"文件{source_path}不存在")

bx_dict = {}

for i in data_list:
    if i[1] in bx_dict.keys():
        bx_dict[i[1]]['sum'] += float(i[4])
        if i[2] in bx_dict[i[1]].keys():
            bx_dict[i[1]][i[2]] += float(i[4])
        else:
            bx_dict[i[1]][i[2]] = float(i[4])
    else:
        tmp = {}
        tmp['sum'] = float(i[4])
        tmp[i[2]] = float(i[4])
        bx_dict[i[1]] = tmp

# print(bx_dict)
bx_list = sorted(bx_dict.items()
                 , key=lambda x : x[1]['sum']
                 , reverse=True)
print(bx_list[0:3])