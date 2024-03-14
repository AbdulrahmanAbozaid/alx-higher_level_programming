-- NUmbe
SELECT tv_genres.name as genre, COUNT(tv_show_genres.show_id) as "number_of_shows" FROM tv_genres INNER
 JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY COUNT(tv_show_genres.show_id) DESC;
