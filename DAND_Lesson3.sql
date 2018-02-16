##SELECT

/*
use * to mean 'all'
*/

SELECT *
FROM table_name

##General Formatting
/*
CAPITALIZE commands and keep everythinhg else lowercase
*/

SELECT column_name FROM table_name;

/*
is the same as
*/

SELECT column_name 
FROM table_name;

/*
just don't forget the closing semicolon!
*/

##LIMIT
/*
use LIMIT to limit the number of rows your query returns, note that LIMIT always goes last:
*/

SELECT column_name 
FROM table_name
LIMIT 15;

##ORDER BY
/*
use ORDER BY to sort column
-defaults to ascending (or alphabetical)
-placed after SELECT and FROM, but before LIMIT
-add DESC after column in ORDER BY statement to sort by descending
-don't forget the space (not ORDERBY)
*/

SELECT column_name
FROM table_name
ORDER BY column_name DESC; 

/*
Q1
Write a query to return the 10 earliest orders in the orders table. 
Include the id, occurred_at, and total_amt_usd.
*/

SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at
LIMIT 10;

/*
Q2
Write a query to return the top 5 orders in terms of largest total_amt_usd. 
Include the id, account_id, and total_amt_usd.
*/

SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC
LIMIT 5;

/*
Q3
Write a query to return the bottom 20 orders in terms of least total. 
Include the id, account_id, and total.
*/

SELECT id, account_id, total
FROM orders
ORDER BY total
LIMIT 20;

/*
Sorting by more than one column:
    list in order you want sorted
*/

SELECT id, account_id, total
FROM orders
ORDER BY account_id, total DESC
LIMIT 20;

/*
Q1
Write a query that returns the top 5 rows from orders ordered according to newest to oldest, but with the largest total_amt_usd for each date listed first for each date. You will notice each of these dates shows up as unique because of the time element. When you learn about truncating dates in a later lesson, you will better be able to tackle this question on a day, month, or yearly basis.
*/

SELECT total_amt_usd, occurred_at
FROM orders
ORDER BY occurred_at DESC, total_amt_usd DESC
LIMIT 5;

/*
Q2
Write a query that returns the top 10 rows from orders ordered according to oldest to newest, but with the smallest total_amt_usd for each date listed first for each date. You will notice each of these dates shows up as unique because of the time element. When you learn about truncating dates in a later lesson, you will better be able to tackle this question on a day, month, or yearly basis. 
*/

SELECT occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at, total_amt_usd 
LIMIT 10;

##WHERE

/*
WHERE allows you to filter a set of results based on specific criteria (ex. a customer id, 4251)
-goes after FROM but before ORDER BY or LIMIT
*/

SELECT column_name
FROM table_name
WHERE account_id = 4251
ORDER BY occurred_at
LIMIT 200;

/* 
you can also use other common symbols with WHERE statements:
>, <, >=, <=, != (not equal to)
*/

/*
Q1
Pull the first 5 rows and all columns from the orders table that have a dollar amount of gloss_amt_usd greater than or equal to 1000.
*/

SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5;

/*
Q2
Pull the first 10 rows and all columns from the orders table that have a total_amt_usd less than 500.
*/

SELECT *
FROM orders
WHERE total_amt_usd < 500
LIMIT 10;

##Using WHERE with non-numeric data

/*
For non-numeric data, you must put the value in single quotes ('cat')

Obviously, this only works with = and != operators
*/

SELECT column_name
FROM table_name
WHERE customer = 'Happy Time';

/*
Q
Filter the accounts table to include the company name, website, and the primary point of contact (primary_poc) for Exxon Mobil in the accounts table.
*/

SELECT name, website, primary_poc
FROM accounts
WHERE name = 'Exxon Mobil';

##Arithmetic operators

/*
Create a new ''derived column' using SELECT and arithmetic operator

Derived columns are manipulations of existing columns in the database

Operators include: *, +, -, /d
*/

SELECT column1, column2, column1 + column2
FROM table_name;

/*
to name your derived column (give it an alias) as AS to the end of the line that produces the derived column and then giving it a name

make sure column names are descriptive, follow existing conventions, and don't include capital letters or spaces
*/

SELECT  column1, 
        column2, 
        column1 + column2 AS new_column_name
FROM table_name;

/*
Q1 using the orders table
Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order. Limit the results to the first 10 orders, and include the id and account_id fields. 
*/

SELECT  id, 
        account_id,
        standard_amt_usd,
        standard_qty,
        standard_amt_usd / standard_qty AS unit_price
FROM orders
LIMIT 10;

/* NOTE FROM SOLUTION
you don't need to SELECT the columns before manipulating them, unless you want to!
*/

SELECT  id, 
        account_id,
        standard_amt_usd / standard_qty AS unit_price
FROM orders
LIMIT 10;

/*
Q2 using orders table
Write a query that finds the percentage of revenue that comes from poster paper for each order. You will need to use only the columns that end with _usd. (Try to do this without using the total column). Include the id and account_id fields. NOTE - you will be thrown an error with the correct solution to this question. This is for a division by zero. You will learn how to get a solution without an error to this query when you learn about CASE statements in a later section. For now, you might just add some very small value to your denominator as a work around.
*/

SELECT  id,
        account_id,
        poster_amt_usd / (standard_amt_usd + gloss_amt_usd + poster_amt_usd) * 100 AS percent_poster_revenue
FROM orders;

##Intro to Logical Operators

/*
LIKE is similar to WHERE, but for situations when you might not know exactly what you are looking for

IN can be used for more than one condition

NOT is used with IN and LIKE to select all of the rows NOT LIKE or NOT IN a certain condition

AND & BETWEEN allow you to combine operations where all combined conditions must be true

OR allows you to combine operations where at least one of the combined conditions must be true
*/

##LIKE

/*
LIKE operator is used to filter within a WHERE clause

requires the use of wild cards (%)

to query URLs that contain 'google' but don't start or end with it, include % on either end use '%google%'

if it starts with google use 'google%'

if it ends with google use '%google'

% can represent any number of characters

within the single quotes, the query is case sensitive, 't' != 'T'
*/

/*
Q1 using the accounts table find...
All the companies whose names start with 'C'. 
*/

SELECT name
FROM accounts
WHERE name LIKE 'C%';

/*
Q2 using accounts table
All companies whose names contain the string 'one' somewhere
*/

SELECT name
FROM accounts
WHERE name LIKE '%one%';

/*
Q3 using accounts table
All companies whose names end with 's'
*/

SELECT name
FROM accounts
WHERE name LIKE '%s';

##IN

/*
IN operator allows you to filter data based on several possible values (values are provided in parenthetical list)

Remember: non numerical data requires single quotation marks!
*/

SELECT column_name
FROM table_name
WHERE column_name IN ('Walmart', 'Apple');

/*
Q1 
Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.
*/

SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name IN ('Walmart', 'Target', 'Nordstrom');

/*
Q2
Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords
*/

SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords');

##NOT

/*
NOT provides the inverse results for IN, LIKE, etc. operators
*/

/*
Q1
Use the accounts table to find the account name, primary poc, and sales rep id for all stores except Walmart, Target, and Nordstrom.
*/

SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name NOT IN ('Walmart', 'Target', 'Nordstrom');

/*
etc.... (remaining questions are just inverse of previous IN and LIKE questions)
*/

##AND and BETWEEN

/*
AND is used to filter based upon multiple criteria

Used within a WHERE statement to consider more than one logical clause at a time

Each time you link a new statement with an AND, you need to specify the column you are interested in

AND work with arithmetic operators, LIKE, IN, and NOT

BETWEEN is used when you want to filter the same column for different parts of the AND statement (before date1 and after date 2, for example)
*/

/*
Q1
Write a query that returns all the orders where the standard_qty is over 1000, the poster_qty is 0, and the gloss_qty is 0.
*/

SELECT standard_qty, poster_qty, gloss_qty
FROM orders
WHERE standard_qty > 1000 AND poster_qty = 0 AND gloss_qty = 0;

/*
Q2
Using the accounts table find all the companies whose names do not start with 'C' and end with 's'.
*/

SELECT name
FROM accounts
WHERE name NOT LIKE 'C%' AND name LIKE '%s';

/*
Q3
Use the web_events table to find all information regarding individuals who were contacted via organic or adwords and started their account at any point in 2016 sorted from newest to oldest.
*/

SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords') AND occurred_at LIKE 2016-%
ORDER BY occurred_at DESC;

/*
Didn't get this one =(

Notes from solution:

BETWEEN is inclusive of endpoints, it assumes the time is at 00:00:00 (midnight) which means, to get all info for 2016, you have to set endpoint at 2017-01-01
*/

SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords') AND occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
ORDER BY occurred_at DESC;

##OR

/*
OR allows you to select rows that satisfy either of two conditions

(AND requires both conditions be satisfied)

each time you link a new statement with an OR, you need to specify the column you are interested in

you can link as many statements as you like

OR works with arithmetic, LIKE, IN, NOT, AND, and BETWEEN

just like with arithmetic operations, the use of parentheses ensires that the logic is being executed correctly
*/

/*
Q1
Find list of orders ids where either gloss_qty or poster_qty is greater than 4000. Only include the id field in the resulting table.
*/

SELECT id
FROM orders
WHERE gloss_qty > 4000 OR poster_qty > 4000;

/*
Q2
Write a query that returns a list of orders where the standard_qty is zero and either the gloss_qty or poster_qty is over 1000.
*/

SELECT *
FROM orders
WHERE standard_qty = 0 AND (gloss_qty > 1000 OR poster_qty >1000);

/*
Q3
Find all the company names that start with a 'C' or 'W', and the primary contact contains 'ana' or 'Ana', but it doesn't contain 'eana'.
*/

SELECT name, primary_poc
FROM accounts
WHERE (name LIKE 'C%' OR name LIKE 'W%') AND (primary_poc LIKE '%ana%' OR primary_poc LIKE '%Ana%' AND primary_poc NOT LIKE '%eana%');

##MOVING AVERAGES

/*
useful for smoothing out daily volatility while allowing you to observe long term trends in data (ex shopping trends)

Use the provided spreadsheet to calculate some moving averages

(7 day moving average is average of 7 days including current day, etc.)
*/


