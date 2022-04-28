-- companies
-- symbol, a string of the stock symbol that is the primary key of this table
-- name, a string of the company name
-- location, a string of the company's HQ location

-- quotes
-- symbol, a string of the stock symbol that is the primary key of this table
-- prev_close, the previous closing price of this stock, a number
-- price, the current stock price, a number
-- avg_price, the average closing price over the last five days, a number
-- volume, the volume of this stock as a number
-- change_pct, the percent change in the stock’s price today, as a decimal

-- Write a SQL statement to return each state and number of companies headquartered 
-- in that state (no need to include states not in your dataset). 
-- Order alphabetically by location (A -> Z).
SELECT companies.location, COUNT(companies.symbol)
FROM companies
LEFT JOIN quotes ON companies.symbol == quotes.symbol
GROUP BY companies.location
ORDER BY companies.location ASC;