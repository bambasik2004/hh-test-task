SELECT 
    MONTH(creation_time) AS month,
    COUNT(*) AS vacancy_count 
FROM 
    vacancy 
WHERE 
    LOWER(name) LIKE '%водитель%' 
    AND work_schedule = 'Гибкий график' 
    AND YEAR(creation_time) BETWEEN 2020 and 2021
    AND disabled = FALSE
GROUP BY 
    MONTH(creation_time)
ORDER BY 
    month;
