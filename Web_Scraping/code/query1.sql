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

-- Write a SQL statement to return the symbol and name of the stock with the 
-- biggest percent gain relative to its five day average price. This should be 
-- calculated as the current price divided by the average price.

SELECT companies.symbol, name
FROM companies
LEFT JOIN quotes ON companies.symbol == quotes.symbol
ORDER BY (price/avg_price) DESC
LIMIT 1;