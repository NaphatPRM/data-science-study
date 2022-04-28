/*
Write a SQL query that returns the name of director and 
a boolean value if the director has directed more than or
equal to 5 movies. The boolean value will be 1 if true else 0.

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));

*/

SELECT primary_name,
CASE WHEN COUNT(primary_title) >= 5 THEN 1
ELSE 0 END AS boolean_directed
FROM names
INNER JOIN crews ON names.nconst == crews.director
INNER JOIN titles ON crews.tconst == titles.tconst
GROUP BY primary_name;