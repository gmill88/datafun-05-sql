--finds the average year published and the earliest published book
SELECT
    AVG(year_published),
    MIN(year_published)
    FROM books;