/* 
Write a SQL query that finds primary_title, avg_rating and 
reviews of 20 movies. The reviews depend on average rating. 
A movie with rating less than or equal to 3 should be reviewed as 'poor'. 
A movie with rating greater than 3 and less than or equal to 6 should be 
reviewed as 'okay' and a movie with rating greater than 6 should 
be reviewed as 'good'. 
The result should be sorted by the title (descending order)

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));

(Hint: The CASE function may come in handy)
*/
SELECT primary_title, avg_rating, 
CASE WHEN avg_rating <= 3 THEN 'poor'
WHEN avg_rating > 3 AND avg_rating <= 6 THEN 'okay'
ELSE 'good' END AS reviews
FROM titles
INNER JOIN ratings ON titles.tconst == ratings.tconst
ORDER BY primary_title DESC
LIMIT 20