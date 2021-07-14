-- Lists all shows that have at least one genre linked
SELECT title, name
FROM tv_shows LEFT JOIN
(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id ORDER BY title, name;
