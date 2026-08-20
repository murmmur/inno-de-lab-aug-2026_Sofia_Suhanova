--Выведите список доставок со статусом и именем клиента.
select s.status, c.first_name, c.last_name
from Shippings s
join Customers c on s.customer=c.customer_id;