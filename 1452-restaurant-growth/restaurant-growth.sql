# Write your MySQL query statement below
WITH daily_amount AS (
    SELECT
        visited_on,
        SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
moving_sum AS (
    SELECT
        visited_on,
        SUM(total_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        COUNT(*) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS day_count
    FROM daily_amount
)
SELECT
    visited_on,
    amount,
    ROUND(amount / 7, 2) AS average_amount
FROM moving_sum
WHERE day_count = 7
ORDER BY visited_on;