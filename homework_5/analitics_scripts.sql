--Аналитические запросы

--1. Количество приемов по месяцам
select d.year,
d.month_name,
count (*) as total_appointments
from fact_appointments f
join dim_date d on f.date_sk=d.date_sk 
group by d.year, d.month_name, d.day_of_week 
order by d.year, d.month;

--2.Какой врач принял больше всего питомцев?
select doc.full_name,
count (*) as total_appointments
from fact_appointments f
join dim_doctor doc on f.doctor_sk=doc.doctor_sk 
group by doc.full_name 
order by total_appointments desc 
limit 1;

--3.Самые частые диагнозы
select diag.diagnosis_name
count (*) as frequency
from fact_appointments f
join dim_diagnosis diag on f.diagnosis_sk=diag.diagnosis_sk 
group by diag.diagnosis_name 
order by frequency desc;

--4 Общая выручка по врачам за 2026 год
select doc.full_name
sum(f.total_cost) as total_revenue,
count (*) as appointments_count
from fact_appointments f
join dim_doctor doc on f.doctor_sk=doc.doctor_sk 
join dim_date d on f.date_sk=d.date_sk 
where d.year=2026
group by by doc.full_name
order by total_revenue desc;