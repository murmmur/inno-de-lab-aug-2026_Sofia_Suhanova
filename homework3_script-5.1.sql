select c.first_name, c.last_name, o.amount
from Customers c
join Orders o on c.customer_id =o.customer_id
where o.amount=(select max(amount) from Orders);
