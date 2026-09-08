SELECT date_date,purchase_cost, ROUND(SUM(turnover),1) AS daily_turnover
FROM data-analytics-469406.course14.gwz_sales
GROUP BY date_date, purchase_cost
ORDER BY date_date;