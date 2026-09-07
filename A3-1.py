# 读取数据将金额大于1000的行写入新文件expenses_large.csv

import csv
from pathlib import Path

source_path = Path(__file__).parent/'practice_data/expenses.csv'
target_path = Path(__file__).parent/'practice_data/expenses_large.csv'

with open(source_path, 'r') as f:
    data_list = list(csv.reader(f))

title = data_list[0]

with open(target_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(title)
    for i in data_list[1:]:
        tmp = float(i[4])
        if tmp >= 1000:
            writer.writerow(i)

