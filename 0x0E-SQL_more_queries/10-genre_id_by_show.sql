-- lists all shows that have at least 1 genre linked
SELECT title, genre_id FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
ORDER BY title, genre_id;
