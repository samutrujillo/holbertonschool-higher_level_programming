-- Lists all genres from hbtn_0d_tvshows with comedy genre
SELECT title FROM tv_genres INNER JOIN
(tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
ON tv_genres.id = tv_show_genres.genre_id WHERE name = 'Comedy'
ORDER BY title;
