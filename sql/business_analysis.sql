-- ============================================
-- SMART DATA MODERNIZATION
-- BUSINESS ANALYSIS QUERIES
-- ============================================

-- 1. Total Sales, Profit and Quantity
SELECT
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM superstore;


-- 2. Category-wise Sales and Profit
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM superstore
GROUP BY category
ORDER BY total_profit DESC;


-- 3. Year-wise Business Performance
SELECT
    year,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM superstore
GROUP BY year
ORDER BY year;


-- 4. Region-wise Performance
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM superstore
GROUP BY region
ORDER BY total_profit DESC;


-- 5. Shipping Mode Analysis
SELECT
    ship_mode,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    AVG(shipping_days) AS average_shipping_days
FROM superstore
GROUP BY ship_mode
ORDER BY total_sales DESC;


-- 6. Top 10 Customers by Profit
SELECT
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM superstore
GROUP BY customer_name
ORDER BY total_profit DESC
LIMIT 10;


-- 7. Loss-Making Sub-Categories
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM superstore
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;


-- 8. Product Category Performance
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(
        SUM(profit) * 100.0 / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin
FROM superstore
GROUP BY category
ORDER BY profit_margin DESC;


-- 9. Discount vs Profit
SELECT
    discount,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(profit) AS average_profit
FROM superstore
GROUP BY discount
ORDER BY discount;


-- 10. Highest Sales Products
SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;