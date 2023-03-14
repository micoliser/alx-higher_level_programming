-- list records of table second table that has score >= 10
-- only fields score and name is displayed
-- score is sorted highest to lowest
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
