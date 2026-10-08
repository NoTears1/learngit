select customer_name, count(order_id) '笔数' 
from customers c 
left join orders o on c.customer_id = o.customer_id
group by customer_name