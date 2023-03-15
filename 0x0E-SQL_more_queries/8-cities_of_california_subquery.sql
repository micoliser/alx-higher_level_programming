-- lists all cities of california in database
SELECT state_id AS 'id', name FROM cities
WHERE state_id = (SELECT id FROM states
	WHERE states.name = 'California')
ORDER BY cities.id;
