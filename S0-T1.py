# 列：单据号,员工,费用类型,城市,金额,日期

# 要求（标准库 csv 就够，不用 pandas）：

# 用 utf-8-sig 读取（这个文件带 BOM，用 utf-8 读第一列的键会变成单据号）
# 按员工分组统计：有效记录数、金额合计（保留 2 位）、金额平均
# 同时列出金额无法转成数字的问题记录（打印单据号 + 原始值即可）
# 统计算"有效记录"时排除问题记录

import csv
from pathlib import Path

source = Path(__file__).parent/'practice_data/expenses_dirty.csv'

with open(source, 'r') as f:
    raw_data = list(csv.reader(f.readlines()))

title = raw_data[0]
data = raw_data[1:]

staff = {}
error_line = 0
error_lines = []
total = 0

j = 1 

for line in data:
    j += 1
    line.append(j)
    try:
        num = float(line[4])
    except ValueError:
        error_line += 1
        error_lines.append(line)
        error_lines[-1].append('金额格式错误或非数字')
    # if num < 0:
    #     error_line += 1
    #     error_lines.append(line)
    else:
        flag = True
        for item in line:
            if item == '':
                error_line += 1
                error_lines.append(line)
                error_lines[-1].append('存在空字段')
                flag = False
                break
        if flag == True:
            if line[1] in staff.keys():
                staff[line[1]][0] += num
                staff[line[1]][1] = int(staff[line[1]][1]) + 1
                total += num
            else :
                staff[line[1]] = [num, 1]
                total += num

print('== 数据读取 ==\n')
print(f'总行数（不含表头）：{len(data)}\n')
print(f'有效记录数：{len(data)-error_line}\n')
print(f'问题记录数：{error_line}\n\n')
print('== 按员工汇总（仅有效记录） ==\n')
print('员工  笔数  金额合计  金额平均\n------------------------------\n')
for key, item in staff.items():
    print(f'{key}  {item[1]}  {item[0]}  {float(item[0])/float(item[1]):.2f}\n')
print(f'-----------------------------\n合计  {len(data)-error_line}  {total:.2f}\n\n')
print('== 问题记录 == \n')
for i in range(len(error_lines)) :
    print(f'行号：{error_lines[i][-2]}  单据号：{error_lines[i][0]} 金额：{error_lines[i][4]}  原因：{error_lines[i][-1]}')

#