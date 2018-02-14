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
