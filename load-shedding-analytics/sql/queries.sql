-- queries.sql
-- Key analytical queries used in the project. Each is written to answer a
-- specific business question - this is the set you should be ready to walk
-- through, explain, and adapt live in an interview.

-- 1. Which years were worst overall, by average stage?
SELECT year,
       ROUND(AVG(stage), 2) AS avg_stage,
       ROUND(SUM(hours_shed), 0) AS total_hours_shed,
       ROUND(SUM(est_business_cost_zar), 0) AS total_est_cost_zar
FROM load_shedding_daily
GROUP BY year
ORDER BY year;

-- 2. How many days per year were "severe" (stage 4 or higher)?
SELECT year,
       COUNT(*) AS severe_days
FROM load_shedding_daily
WHERE stage >= 4
GROUP BY year
ORDER BY year;

-- 3. Winter vs summer comparison: does load-shedding really get worse in winter?
SELECT season,
       ROUND(AVG(stage), 2) AS avg_stage,
       ROUND(AVG(hours_shed), 2) AS avg_daily_hours
FROM load_shedding_daily
GROUP BY season;

-- 4. Month-by-month trend across all years (seasonality pattern).
SELECT month,
       ROUND(AVG(stage), 2) AS avg_stage
FROM load_shedding_daily
GROUP BY month
ORDER BY month;

-- 5. Rolling improvement check: 90-day moving average of stage over time
--    (SQLite window function - shows the trend line used in the dashboard).
SELECT date,
       stage,
       ROUND(AVG(stage) OVER (
           ORDER BY date
           ROWS BETWEEN 89 PRECEDING AND CURRENT ROW
       ), 2) AS rolling_90day_avg_stage
FROM load_shedding_daily
ORDER BY date;

-- 6. Total estimated cost to a small business over the full period.
SELECT ROUND(SUM(est_business_cost_zar), 0) AS total_est_cost_zar,
       ROUND(SUM(hours_shed), 0) AS total_hours_shed
FROM load_shedding_daily;
