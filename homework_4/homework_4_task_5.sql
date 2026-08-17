--Task 5
/*
 1. Функция: Создать функцию PostgreSQL с именем 
CalculateAnnualBonus, которая принимает employee_id и 
Salary  в качестве входных данных и возвращает рассчитанную 
сумму бонуса (10 % от Salary) для этого сотрудника. Используйте 
PL/pgSQL для тела функции. 
2. Использовать эту функцию в операторе SELECT, чтобы увидеть 
потенциальный бонус для каждого сотрудника. 
3. Представление (View): Создать представление с именем 
IT_Department_View, которое показывает EmployeeID, 
FirstName, LastName и Salary только для сотрудников из отдела 
'IT'. 
4. Выбрать данные из вашего представления IT_Department_View.
*/

--1
create or replace function CalculateAnnualBonus(employee_id INT, Salary DECIMAL (10,2))
returns decimal
language plpgsql
as $$
declare 
bonus decimal(10,2);
begin
bonus:=Salary*0.1;
return bonus;
end;
$$;

--2
select FirstName, LastName, Department, Salary, CalculateAnnualBonus(EmployeeID, Salary) as Bonus
from Employees;

--3
create view IT_Department_View as 
select EmployeeID, FirstName, LastName, Salary
from Employees 
where Department='IT';

--4
select * from IT_Department_View;
