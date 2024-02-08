-- combines info from author and books tables
SELECT *
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;