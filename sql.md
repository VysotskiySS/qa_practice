

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
