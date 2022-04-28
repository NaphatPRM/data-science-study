/*
Write an SQL query that returns the decades and 
percentage of titles which were released in the 
corresponding decade

CREATE TABLE names(nconst text primary key, primary_name text, birth_year integer, death_year integer);
CREATE TABLE ratings(tconst text primary key, avg_rating real, num_votes integer);
CREATE TABLE crews(id integer primary key autoincrement, tconst text, director text, foreign key(director) references names(nconst));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE titles(tconst text primary key, type text, primary_title text, original_title text, start_year int, end_year int, runtime_minutes int);
CREATE TABLE title_genres(tconst text, genre text, primary key(tconst, genre));

*/

SELECT DISTINCT (start_year/10)*10 AS decade, percent_decade
FROM titles
INNER JOIN (SELECT start_year/10 as decade_per, COUNT(start_year/10) * 100.0 / (SELECT COUNT(start_year/10) from titles) as percent_decade
FROM titles GROUP BY start_year/10) per_table
ON titles.start_year/10 == per_table.decade_per
