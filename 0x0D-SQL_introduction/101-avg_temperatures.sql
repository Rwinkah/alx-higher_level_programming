-- calc average temperature and sort by avg temp
SELECT city, AVG(value) AS avg_temp FROM temperatures ORDER BY avg_temp DESC;
