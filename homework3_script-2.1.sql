--Получите список заказов вместе с именем клиента, который сделал заказ.
select c.first_name, c.last_name, o.item, o.amount
from Customers c
join Orders o on c.customer_id=o.customer_id;
