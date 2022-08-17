
![44](https://user-images.githubusercontent.com/109433447/185190292-024dd410-703c-4025-a9c2-941b437b4fd2.PNG)
  
- Найдите максимальный возраст (колич. лет) среди обучающихся 10 классов?
  
``` sql
SELECT MAX(FLOOR(DATEDIFF(CURDATE(), birthday)/365)) AS max_year
FROM Student INNER JOIN Student_in_class
ON Student.id = Student_in_class.student
	INNER JOIN Class
	ON Student_in_class.class = Class.id
WHERE name LIKE '10 %';
```
- Какой(ие) кабинет(ы) пользуются самым большим спросом?
  
 
``` sql
SELECT classroom 
FROM Schedule
GROUP BY classroom 
HAVING COUNT(classroom) = (
    SELECT MAX(count_pair)
    FROM (
        SELECT COUNT(id) AS count_pair
        FROM Schedule
        GROUP BY classroom
    ) AS querry
    
);

```

- Выведите фамилии преподавателей, которые ведут физическую культуру (Physical Culture). Отcортируйте преподавателей по фамилии.
  
``` sql
SELECT last_name 
FROM Teacher JOIN Schedule 
	ON Teacher.id = Schedule.teacher 
JOIN Subject 
	ON Schedule.subject = Subject.id
WHERE Subject.name = 'Physical Culture'
ORDER BY last_name
```
 
![55](https://user-images.githubusercontent.com/109433447/184479525-db8d7888-0516-4828-a5ad-63c7812046d5.PNG)
  
- Удалить компании, совершившие наименьшее количество рейсов.
``` sql
DELETE Company 
FROM Company INNER JOIN (
	SELECT name FROM Company INNER JOIN Trip
	ON Company.id = Trip.company
	GROUP BY company
	HAVING COUNT(Trip.id) = (
		SELECT MIN(count) AS min_count
		FROM (
			SELECT name, count 
			FROM Company INNER JOIN (
				SELECT company, COUNT(id) AS count
				FROM Trip
				GROUP BY company
			) AS Query
			ON Company.id = Query.company) AS Query_2
		)) AS Query_3
	ON Company.name = Query_3.name	
```
