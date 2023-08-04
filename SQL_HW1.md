## HW_1
1) Создать таблицу employees
- id. serial, primary key,
- employee_name. Varchar(50), not null
```
create table employees(
	id serial primary key,
	employee_name varchar(50) not null
);
```
2) Наполнить таблицу employee 70 строками.
```
insert into employees(employee_name)
values ('Ашра'),
('Барака'),
('Бо Рай Чо'),
('Горо'),
('Дайро'),
('Дарк Кан'),
('Дарксайд'),
('Детстроук'),
('Джакс'),
('Джонни Кейдж'),
('Ди’Вора'),
('Драмин'),
('Дэйгон'),
('Кабал'),
('Кай'),
('Камелеона'),
('Кано'),
('Кинтаро'),
('Кира'),
('Китана'),
('Кобра'),
('Коталь Кан'),
('Кратос'),
('Кроника'),
('Куан Чи'),
('Кун Лао'),
('Кун Цзинь'),
('Кэнси'),
('Кэсси Кейдж'),
('Ли Мэй'),
('Лю Кан'),
('Мавадо'),
('Милина'),
('Миротворец'),
('Мит'),
('Мокап'),
('Молох'),
('Мотаро'),
('Нитара'),
('Ночной Волк'),
('Нуб Сайбот'),
('Райдэн'),
('Рейн'),
('Рептилия'),
('Рэйко'),
('Саб-Зиро'),
('Сайракс'),
('Сарина'),
('Сектор'),
('Синдел'),
('Скорпион'),
('Смоук'),
('Соня Блейд'),
('Страйкер'),
('Сюй Хао'),
('Такэда'),
('Тремор'),
('Триборг'),
('Тэйвен'),
('Флэш'),
('Фрост'),
('Фудзин'),
('Хавик'),
('Хамелеон'),
('Хотару'),
('Шан Цзун'),
('Шао Кан'),
('Шива'),
('Шиннок'),
('Эрмак');
```
3) Создать таблицу salary
- id. Serial primary key,
- monthly_salary. Int, not null
```
create table salary(
	id serial primary key,
	monthly_salary int not null
);
```
4) Наполнить таблицу salary 15 строками:
- 1000
- 1100
- 1200
- 1300
- 1400
- 1500
- 1600
- 1700
- 1800
- 1900
- 2000
- 2100
- 2200
- 2300
- 2400
- 2500

```
insert into salary(monthly_salary)
values
('1000'),
('1100'),
('1200'),
('1300'),
('1400'),
('1500'),
('1600'),
('1700'),
('1800'),
('1900'),
('2000'),
('2100'),
('2200'),
('2300'),
('2400'),
('2500');
```
5) Создать таблицу employee_salary
- id. Serial primary key,
- employee_id. Int, not nu
```
create table employee_salary(
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null
);
```
6) Наполнить таблицу employee_salary 40 строками:
- в 10 строк из 40 вставить несуществующие employee_id

```
insert into employee_salary(employee_id, salary_id)
values (1,1),
	   (51,2),
	   (80,3),
	   (52,4),
	   (3,5),
	   (53,15),
	   (4,14),
	   (76,13),
	   (5,12),
	   (55,11),
	   (6,7),
	   (32,7),
	   (75,8),
	   (8,9),
	   (34,10),
	   (9,10),
	   (36,9),
	   (10,8),
	   (38,7),
	   (74,6),
	   (40,5),
	   (79,15),
	   (22,11),
	   (18,12),
	   (73,13),
	   (19,14),
	   (25,15),
	   (78,14),
	   (65,13),
	   (26,12),
	   (64,11),
	   (27,10),
	   (77,9),
	   (28,8),
	   (62,7),
	   (29,5),
	   (61,4),
	   (30,3),
	   (71,2),
	   (72,1);
```

```
select employee_name, monthly_salary
from employees join employee_salary
on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id 
order by employee_name;
```
7) Создать таблицу roles
- id. Serial primary key,
- role_name. int, not null, unique
```
create table roles(
	id serial primary key,
	role_name int not null unique
);
```
8) Поменять тип столба role_name с int на varchar(30)

```
alter table roles alter column role_name type varchar(30);
```
9) Наполнить таблицу roles 20 строками:
id role_name
1 Junior Python developer
2 Middle Python developer
3 Senior Python developer
4 Junior Java developer
5 Middle Java developer
6 Senior Java developer
7 Junior JavaScript developer
8 Middle JavaScript developer
9 Senior JavaScript developer
10 Junior Manual QA engineer
11 Middle Manual QA engineer
12 Senior Manual QA engineer
13 Project Manager
14 Designer
15 HR
16 CEO
17 Sales manager
18 Junior Automation QA engineer
19 Middle Automation QA engineer
20 Senior Automation QA engineer
```
insert into roles(role_name)
values 	('Junior Python developer'),
		('Middle Python developer'),
		('Senior Python developer'),
		('Junior Java developer'),
		('Middle Java developer'),
		('Senior Java developer'),
		('Junior JavaScript developer'),
		('Middle JavaScript developer'),
		('Senior JavaScript developer'),
		('Junior Manual QA engineer'),
		('Middle Manual QA engineer'),
		('Senior Manual QA engineer'),
		('Project Manager'),
		('Designer'),
		('HR'),
		('CEO'),
		('Sales manager'),
		('Junior Automation QA engineer'),
		('Middle Automation QA engineer'),
		('Senior Automation QA engineer');
```	
10) Создать таблицу roles_employee
- id. Serial primary key,
- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
- role_id. Int, not null (внешний ключ для таблицы roles, поле id)

```
create table roles_employee(
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key (employee_id) references employees(id),
	foreign key (role_id) references roles(id)
);	
```
11) Наполнить таблицу roles_employee 40 строками:

```
insert into roles_employee (employee_id, role_id)
values  (3,1),
		(1,2),
		(4,5),
		(5,8),
		(7,2),
		(9,1),
		(11,10),
		(13,11),
		(22,13),
		(32,12),
		(65,14),
		(36,12),
		(28,14),
		(10,15),
		(20,3),
		(30,3),
		(40,1),
		(50,4),
		(60,17),
		(70,18),
		(35,15),
		(37,11),
		(47,13),
		(48,17),
		(51,14),
		(52,16),
		(53,19),
		(54,20),
		(56,15),
		(57,12),
		(43,14),
		(8,15),
		(68,9),
		(21,7),
		(55,16),
		(49,3),
		(46,6),
		(38,7),
		(64,8),
		(19,14);
```
## HW_2

1. Вывести все поля и все строки;
```
select * from students;
```
3. Вывести всех студентов в таблице;
```
select distinct name
from students;
```
4. Вывести только Id пользователей;
```
select id from students;
```
5. Вывести только имя пользователей;
```
select name from students;
```
6. Вывести только email пользователей;
```
select email from students;
```
7. Вывести имя и email пользователей;
```
select name, email from students;
```
8. Вывести id, имя, email и дату создания пользователей;
```
select id, name, email, created_on from students;
```
9. Вывести пользователей где password 12333;
```
select * from students
where password = '12333';
```
10. Вывести пользователей которые были созданы 2021-03-26 00:00:00;
```
select * from students
where created_on = '2021-03-26 00:00:00';
```
11. Вывести пользователей где в имени есть слово Анна;
```
select * from students
where name like '%Anna%';
```
12. Вывести пользователей где в имени в конце есть 8;
```
select * from students
where name like '%8';
```
13. Вывести пользователей где в имени в есть буква а;
```
select * from students
where name like '%a%';
```
14. Вывести пользователей которые были созданы 2021-07-12 00:00:00;
```
select * from students
where created_on = '2021-07-12 00:00:00';
```
15. Вывести пользователей которые были созданы 2021-07-12 00:00:00 и имеют пароль 1m313;
```
select * from students
where created_on = '2021-07-12 00:00:00' and password = '1m313';
```
16. Вывести пользователей которые были созданы 2021-07-12 00:00:00 и у которых в имени есть слово Andrey;
```
select * from students
where created_on = '2021-07-12 00:00:00' and name like '%Andrey%';
```
17. Вывести пользователей которые были созданы 2021-07-12 00:00:00 и у которых в имени есть цифра 8;
```
select * from students
where created_on = '2021-07-12 00:00:00' and name like '%8%';
```
18. Вывести пользователя у которых id равен 110;
```
select * from students
where id = '110';
```
19. Вывести пользователя у которых id равен 153;
```
select * from students
where id = '153';
```
20. Вывести пользователя у которых id больше 140;
```
select * from students
where id > '110';
```
21. Вывести пользователя у которых id меньше 130;
```
select * from students
where id > '130';
```
22. Вывести пользователя у которых id меньше 127 или больше 188;
```
select * from students
where id < '127' or id > '188';
```
23. Вывести пользователя у которых id меньше либо равно 137;
```
select * from students
where id <= '137';
```
24. Вывести пользователя у которых id больше либо равно 137;
```
select * from students
where id >= '137';
```
25. Вывести пользователя у которых id больше 180 но меньше 190;
```
select * from students
where id > '180' and id < '190';
```
26. Вывести пользователя у которых id между 180 и 190;
```
select * from students
where id BETWEEN '180' and '190';
```
27. Вывести пользователей где password равен 12333, 1m313, 123313;
```
select * from students
where password in ('12333', '1m313', '123313');
```
28. Вывести пользователей где created_on равен 2020-10-03 00:00:00, 2021-05-19 00:00:00, 2021-03-26 00:00:00;
```
select * from students
where created_on in ('2020-10-03 00:00:00', '2021-05-19 00:00:00', '2021-03-26 00:00:00');
```
29. Вывести минимальный id;
```
select min(id) from students;
```
30. Вывести максимальный.;
```
select max(id) from students;
```
31. Вывести количество пользователей;
```
select count(*) from students;
```
32. Вывести id пользователя, имя, дату создания пользователя. Отсортировать по порядку возрастания даты добавления пользоватлеля.;
```
select id, name, created_on from students order by created_on;
```
33. Вывести id пользователя, имя, дату создания пользователя. Отсортировать по порядку убывания даты добавления пользоватлеля.;
```
select id, name, created_on from students order by created_on desc;
```
