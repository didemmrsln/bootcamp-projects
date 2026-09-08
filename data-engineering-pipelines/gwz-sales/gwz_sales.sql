-- Daily turnover by purchase cost, GreenWeez sales (BigQuery).
-- Replace `your-project` with your own GCP project id before running.
SELECT
    date_date,
    purchase_cost,
    ROUND(SUM(turnover), 1) AS daily_turnover
FROM `your-project.course14.gwz_sales`
GROUP BY date_date, purchase_cost
ORDER BY date_date;
