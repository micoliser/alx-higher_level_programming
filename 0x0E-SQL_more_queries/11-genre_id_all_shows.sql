-- lists all shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
ORDER BY title, genre_id;
