/*
Write a sql query to find primary_title of top 10 movies 
which have received an average rating of more than or equal to 8.5,
or have been voted by more than or equal to 1000000 people. The results
should be sorted by the average rating in descending order 

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));
*/
SELECT primary_title
FROM titles
INNER JOIN ratings ON titles.tconst == ratings.tconst
WHERE avg_rating >= 8.5 OR num_votes >= 1000000
ORDER BY avg_rating DESC
LIMIT 10