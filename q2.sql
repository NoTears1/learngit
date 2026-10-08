select customer_name, sum(amount) '已支付金额', count(order_id) '有效笔数'
from customers c
join orders o
on c.customer_id = o.customer_id
where status = 'paid'
group by customer_name