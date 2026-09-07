# 读取含脏数据文件，利用错误处理，提高程序健壮性
# 空行跳过、金额是文本的行记入"坏行清单"、负数金额单独标注；
# 最后 print 三行汇总（成功 n 行 / 坏行 n 行 / 坏行原因分类）
import csv
from pathlib import Path

def load_expenses(path) -> list:
    with open(path, 'r') as f:
        return list(csv.reader(f))

def sum_by(records, key_name) -> dict:
    result = {}
    bad_records = []
    title = records[0]
    try:
        key_no = title.index(key_name)
    except ValueError:
        print(f"字段：“{key_name}”不存在")
        return result

    for record in records[1:]:
        tmp_key = record[key_no]
        try:
            tmp_value = float(record[4])
        except ValueError:
            if record[4] == '':
                print(f"金额为空")
            else:
                print(f"“{record[4]}”不是一个数字")
                bad_records.append(record[0])
        if tmp_value < 0:
            print(f"{record[0]}的金额不能为负数")
            continue
        if tmp_key in result.keys():
            result[tmp_key] += tmp_value
        else:
            result[tmp_key] = tmp_value

    return result, bad_records

source_path = Path(__file__).parent/'practice_data/expenses_dirty.csv'
print(sum_by(load_expenses(source_path),'员工'))