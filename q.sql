CREATE TABLE customers (
  customer_id   TEXT PRIMARY KEY,
  customer_name TEXT NOT NULL,
  region        TEXT
);
CREATE TABLE orders (
  order_id   TEXT,
  customer_id TEXT,
  order_date TEXT,
  amount     REAL,
  status     TEXT
);

INSERT INTO customers VALUES
 ('C1','甲公司','华东'),('C2','乙公司','华北'),
 ('C3','丙公司','华东'),('C4','丁公司','华南');

INSERT INTO orders VALUES
 ('O1','C1','2026-08-01',100.0,'paid'),
 ('O2','C1','2026-08-05',200.0,'cancelled'),
 ('O3','C2','2026-08-07',300.0,'paid'),
 ('O4','C2','2026-08-09',150.0,'paid'),
 ('O5','C2','2026-08-09',150.0,'paid'),   -- 与 O4 重复单号
 ('O6','C9','2026-08-11', 50.0,'paid');   -- C9 不存在