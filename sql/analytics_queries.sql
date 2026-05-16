SELECT * FROM sales_orders;

SELECT category, SUM(total_amount) AS total_revenue
FROM sales_orders
GROUP BY category
ORDER BY total_revenue DESC;

SELECT city, SUM(total_amount) AS city_revenue
FROM sales_orders
GROUP BY city
ORDER BY city_revenue DESC;

SELECT product, SUM(quantity) AS total_quantity_sold
FROM sales_orders
GROUP BY product
ORDER BY total_quantity_sold DESC;

SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS monthly_revenue
FROM sales_orders
GROUP BY month
ORDER BY month;