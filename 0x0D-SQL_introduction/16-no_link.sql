-- lists all records of the table second table
-- not listing rows without a name value
-- sorted by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
