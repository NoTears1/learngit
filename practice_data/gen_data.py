# -*- coding: utf-8 -*-
"""《学习计划7》阶段A 练习数据生成器

用法: python gen_data.py
生成: expenses.csv / expenses_dirty.csv / bank_flow.csv / erp_flow.csv
说明: 固定随机种子，每次生成的数据一致，方便对照练习答案。
"""
import csv
import random
from pathlib import Path

random.seed(7)
HERE = Path(__file__).resolve().parent

EMPLOYEES = ["张伟", "李娜", "王强", "赵敏", "刘洋"]
TYPES = ["差旅-住宿", "差旅-交通", "餐饮", "办公用品", "培训"]
CITIES = ["北京", "上海", "广州", "深圳", "杭州"]


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ---------- 1. 干净的报销明细 ----------
rows = []
for i in range(1, 31):
    rows.append([
        f"BX2026-{i:04d}",
        random.choice(EMPLOYEES),
        random.choice(TYPES),
        random.choice(CITIES),
        round(random.uniform(80, 2800), 2),
        f"2026-08-{random.randint(1, 31):02d}",
    ])
write_csv(HERE / "expenses.csv",
          ["单据号", "员工", "费用类型", "城市", "金额", "日期"], rows)

# ---------- 2. 脏数据版（在干净版基础上人工注入问题） ----------
dirty = [r[:] for r in rows]
dirty[2][4] = "1,234.50"      # 金额含千分位逗号（文本）
dirty[5][4] = ""              # 金额缺失
dirty[7][4] = "待定"          # 金额不是数字
dirty[10][1] = ""             # 员工缺失
dirty[13][4] = "-320.00"      # 负数（可能是冲销单）
dirty[16][5] = "8月17日"      # 日期格式不统一
dirty[19][4] = "1200元"       # 金额带单位
dirty[22][4] = " 890.5 "      # 前后空格
dirty[25][0] = ""             # 单据号缺失
dirty.insert(9, ["", "", "", "", "", ""])   # 全空行
dirty.insert(20, dirty[3][:])               # 完全重复的行
write_csv(HERE / "expenses_dirty.csv",
          ["单据号", "员工", "费用类型", "城市", "金额", "日期"], dirty)

# ---------- 3. 对账数据：银行流水 vs ERP 应付 ----------
erp_rows = rows[:25]  # ERP 只登记了前 25 张单据

bank = []
for idx, r in enumerate(erp_rows):
    amt = r[4]
    if idx == 4:
        amt = round(amt + 100, 2)    # 银行多付 100
    if idx == 11:
        amt = round(amt * 0.9, 2)    # 银行少付 10%
    bank.append([f"PAY2026-{idx + 1:04d}", r[0],
                 f"2026-09-{random.randint(1, 5):02d}", amt, f"报销付款-{r[1]}"])

bank[20][1] = "BX2026-9999"  # 银行流水挂错单据号
bank.append(["PAY2026-0026", "BX2026-0030", "2026-09-05", 666.66, "报销付款-王强"])  # ERP 未登记
bank.append(bank[7][:])      # 银行重复支付（重复行）

write_csv(HERE / "bank_flow.csv",
          ["流水号", "单据号", "付款日期", "付款金额", "摘要"], bank)

erp_out = [[r[0], r[1], r[2], r[4], "待付款" if random.random() < 0.3 else "已付款"]
           for r in erp_rows]
write_csv(HERE / "erp_flow.csv",
          ["单据号", "员工", "费用类型", "应付金额", "状态"], erp_out)

print("已生成 4 个练习数据文件 →", HERE)
