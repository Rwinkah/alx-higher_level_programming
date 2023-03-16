-- list all rows in second_table with name not null
SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
