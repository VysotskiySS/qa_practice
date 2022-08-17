- Найдите максимальный возраст (колич. лет) среди обучающихся 10 классов?
  
![44](https://user-images.githubusercontent.com/109433447/185190292-024dd410-703c-4025-a9c2-941b437b4fd2.PNG)

``` sql
SELECT MAX(FLOOR(DATEDIFF(CURDATE(), birthday)/365)) AS max_year
FROM Student INNER JOIN Student_in_class
ON Student.id = Student_in_class.student
	INNER JOIN Class
	ON Student_in_class.class = Class.id
WHERE name LIKE '10 %';
```

- Удалить компании, совершившие наименьшее количество рейсов.
  
![55](https://user-images.githubusercontent.com/109433447/184479525-db8d7888-0516-4828-a5ad-63c7812046d5.PNG)

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


- Выведите фамилии преподавателей, которые ведут физическую культуру (Physical Culture). Отcортируйте преподавателей по фамилии.
  
![43](https://user-images.githubusercontent.com/109433447/185188576-ad7d84c4-3d94-4d89-8a35-a3a30180f4db.PNG)
``` sql
SELECT last_name 
FROM Teacher JOIN Schedule 
	ON Teacher.id = Schedule.teacher 
JOIN Subject 
	ON Schedule.subject = Subject.id
WHERE Subject.name = 'Physical Culture'
ORDER BY last_name
```
