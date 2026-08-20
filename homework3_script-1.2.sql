--Выведите все заказы, у которых сумма (amount) больше 1000
select order_id, item,amount,customer_id
from Orders
where amount > 1000;