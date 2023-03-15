-- lists all genres from hbtn_0d_tvshows and display the
-- number of shows linked to them
SELECT genres.name AS 'genre', COUNT(shows.show_id) AS 'number_of_shows'
FROM tv_genres AS genres INNER JOIN tv_show_genres AS shows
ON genres.id = shows.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
