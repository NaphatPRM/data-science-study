/*
Write a SQL query that returns the different genres of 
all the movies and average runtime of all genres.

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));

*/
SELECT genre, avg(runtime_minutes)
FROM title_genres
INNER JOIN titles ON title_genres.tconst == titles.tconst
GROUP BY genre