-- List all the genres of the show Dexter
SELECT name FROM tv_shows INNER JOIN
(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
WHERE title='Dexter' ORDER BY name;
