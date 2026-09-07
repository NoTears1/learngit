# 按日期前7位分组统计总额
import csv
from pathlib import Path

source_path = Path(__file__).parent/'practice_data/expenses.csv'

with open(source_path, 'r') as f:
    data_list = list(csv.reader(f))[1:]

result = {}

for i in data_list:
    tmp_month = i[5][:7]
    tmp_money = float(i[4])
    if tmp_month in result.keys():
        result[tmp_month] += tmp_money
    else:
        result[tmp_month] = tmp_money

print(result)