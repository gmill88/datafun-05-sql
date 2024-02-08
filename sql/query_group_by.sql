
-- Query using group by clause
SELECT year_published, COUNT(*) AS published_books
FROM books
GROUP BY year_published
ORDER BY published_books DESC;