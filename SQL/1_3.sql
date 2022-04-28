/* 
Write a SQL query that returns the primary_name of directors and 
count of titles directed by each director. 
Results should be ordered by the count of titles in 
descending order

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));
*/
SELECT primary_name, COUNT(primary_title)
FROM names
INNER JOIN crews ON names.nconst == crews.director
INNER JOIN titles ON crews.tconst == titles.tconst
GROUP BY primary_name
ORDER BY COUNT(primary_title) DESC