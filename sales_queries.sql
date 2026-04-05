-- ============================================================
--  PROJECT 2: Retail Sales Performance Analysis — SQL Queries
-- ============================================================

-- QUERY 1: Overall KPIs
SELECT
    COUNT(*)                            AS Total_Orders,
    ROUND(SUM(Sales), 2)               AS Total_Revenue,
    ROUND(SUM(Profit), 2)              AS Total_Profit,
    ROUND(AVG(Sales), 2)               AS Avg_Order_Value,
    ROUND(SUM(Profit)/SUM(Sales)*100,2) AS Profit_Margin_Pct
FROM sales;

-- QUERY 2: Revenue & Profit by Region
SELECT
    Region,
    COUNT(*)                            AS Orders,
    ROUND(SUM(Sales), 2)               AS Revenue,
    ROUND(SUM(Profit), 2)              AS Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,1) AS Margin_Pct
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;

-- QUERY 3: Best and Worst Performing Categories
SELECT
    Category,
    ROUND(SUM(Sales), 2)               AS Revenue,
    ROUND(SUM(Profit), 2)              AS Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,1) AS Margin_Pct,
    SUM(Quantity)                       AS Units_Sold
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;

-- QUERY 4: Quarterly Revenue Trend
SELECT
    Year,
    Quarter,
    ROUND(SUM(Sales), 2)   AS Revenue,
    ROUND(SUM(Profit), 2)  AS Profit,
    COUNT(*)               AS Orders
FROM sales
GROUP BY Year, Quarter
ORDER BY Year, Quarter;

-- QUERY 5: Impact of Discount on Profitability
SELECT
    CASE
        WHEN Discount = 0         THEN 'No Discount'
        WHEN Discount <= 0.10     THEN 'Low (1-10%)'
        WHEN Discount <= 0.20     THEN 'Medium (11-20%)'
        WHEN Discount <= 0.30     THEN 'High (21-30%)'
        ELSE 'Very High (30%+)'
    END                          AS Discount_Bucket,
    COUNT(*)                     AS Orders,
    ROUND(AVG(Sales), 2)        AS Avg_Sale,
    ROUND(AVG(Profit), 2)       AS Avg_Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,1) AS Margin_Pct
FROM sales
GROUP BY Discount_Bucket
ORDER BY Avg_Profit DESC;

-- QUERY 6: Top 10 Highest Revenue Days
SELECT
    OrderDate,
    COUNT(*)              AS Orders,
    ROUND(SUM(Sales), 2) AS Daily_Revenue,
    ROUND(SUM(Profit),2) AS Daily_Profit
FROM sales
GROUP BY OrderDate
ORDER BY Daily_Revenue DESC
LIMIT 10;

-- QUERY 7: Customer Segment Performance
SELECT
    CustomerSegment,
    COUNT(*)                            AS Orders,
    ROUND(SUM(Sales), 2)               AS Revenue,
    ROUND(AVG(Sales), 2)               AS Avg_Order_Value,
    ROUND(SUM(Profit)/SUM(Sales)*100,1) AS Margin_Pct
FROM sales
GROUP BY CustomerSegment
ORDER BY Revenue DESC;

-- QUERY 8: Shipping Mode vs Profit
SELECT
    ShipMode,
    COUNT(*)                     AS Orders,
    ROUND(AVG(ShippingCost), 2) AS Avg_Shipping_Cost,
    ROUND(AVG(Profit), 2)       AS Avg_Profit,
    ROUND(SUM(Profit),2)        AS Total_Profit
FROM sales
GROUP BY ShipMode
ORDER BY Total_Profit DESC;

-- QUERY 9: Year-over-Year Growth
SELECT
    Year,
    ROUND(SUM(Sales), 2)  AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    COUNT(*)              AS Orders
FROM sales
GROUP BY Year
ORDER BY Year;

-- QUERY 10: Region × Category Revenue Matrix
SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Revenue,
    COUNT(*)             AS Orders
FROM sales
GROUP BY Region, Category
ORDER BY Region, Revenue DESC;
