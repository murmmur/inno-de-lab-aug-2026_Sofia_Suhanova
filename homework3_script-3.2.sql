select item, COUNT(*) as count, AVG(amount) as avg_amount
from Orders 
group by item;