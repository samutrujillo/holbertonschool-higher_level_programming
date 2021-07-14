-- Lists all shows that have at least one genre linked
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY title, genre_id;
