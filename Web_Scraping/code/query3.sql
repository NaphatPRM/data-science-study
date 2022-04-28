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

-- Write a SQL statement to return the symbol and name of all stocks with prices 
-- above $35 and where the absolute difference between the current price and 5 day 
-- average price is less than $5. Your results should be sorted by the absolute 
-- difference between current price and 5 day average price, in ascending order.

SELECT companies.symbol, name
FROM companies
LEFT JOIN quotes ON companies.symbol == quotes.symbol
WHERE price > 35 AND ABS(price - avg_price) < 5
ORDER BY ABS(price - avg_price) ASC;