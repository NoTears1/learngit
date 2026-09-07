# 使用循环计算金额的总额、平均、最大值，并打印
# 单个金额，>=500打印“超标，需主管审批”，否则打印“正常”
# 逐个判断金额，超标打印“单据i：xx元——超标”，最后统计超标张数

import csv
from pathlib import Path

source_path = Path(__file__).parent/'practice_data/expenses.csv'

try:
    with open(source_path, 'r') as f:
        data = csv.reader(f)
        # print(list(data))
        data_list = list(data)
except FileNotFoundError:
    print(f'文件{str(source_path)}不存在')



bx_sum = 0
bx_avg = 0
bx_max = 0
bx_cnt = 0

for i in range(1,len(data_list)):
    tmp = float(data_list[i][4])
    bx_sum += tmp
    if bx_max < tmp:
        bx_max = tmp
    if tmp >= 1000:
        print(f"单据{data_list[i][0]}：{tmp}元，超标")
        bx_cnt += 1

bx_avg = bx_sum/(len(data_list)-1)
print(f"报销金额总额：{bx_sum:.2f}\n报销金额平均：{bx_avg:.2f}\n报销金额最大：{bx_max:.2f}\n超标张数：{bx_cnt}")




