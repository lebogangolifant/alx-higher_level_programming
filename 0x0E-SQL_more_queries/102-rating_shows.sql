-- Lists all shows by their rating.
-- from the hbtn_0d_tvshows_rate database
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
