# 读取银行和erp流水，找出1.银行已付但ERP没登记的单据，2.ERP有但银行没付的单据
# 找出两边单据号相同，但金额不一致的；
# 找出银行里重复的流水（同流水号）
# 问题行写进mismatch_report.csv
# 需注意列表的append()的使用
import csv
from pathlib import Path

parent_path = Path(__file__).parent/'practice_data'
bank_path = parent_path/'bank_flow.csv'
erp_path = parent_path/'erp_flow.csv'

with open(bank_path, 'r') as f:
    bank_data = list(csv.reader(f))

with open(erp_path, 'r') as f:
    erp_data = list(csv.reader(f))[1:]

bank_value = bank_data[1:]
bank_set = set(x[1] for x in bank_value)
erp_set = set(y[0] for y in erp_data)

diff_bank = bank_set - erp_set
diff_erp = erp_set - bank_set

bank_dict = {}
erp_dict = {}
mismatch_result = []

for i in bank_value:
    if i[1] in bank_dict.keys():
        tmp = i
        tmp.append('单据号重复')
        mismatch_result.append(tmp)
    else:
        bank_dict[i[1]] = i
for j in erp_data:
    erp_dict[j[0]] = j



for i in bank_set&erp_set:
    bank_tmp_value = float(bank_dict[i][3])
    erp_tmp_value = float(erp_dict[i][3])

    if abs(bank_tmp_value - erp_tmp_value) > 0.01:
        tmp = bank_dict[i]
        tmp.append('金额差异')
        mismatch_result.append(tmp)

# print(mismatch_result)

with open(parent_path/'mismatch_record.csv', 'w') as f:
    writer = csv.writer(f)
    title = bank_data[0]
    title.append('问题原因')
    writer.writerow(title)
    for m in mismatch_result:
        writer.writerow(m)

print(f"银行已付但ERP没登记：{diff_bank}\nERP有但银行没付：{diff_erp}")


