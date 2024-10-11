SELECT 
    total_vacancies.area_name,
    IF(suitable_count IS NULL, 0, suitable_count) / total_count as proportion_suitable_vacancies
FROM
    (
        SELECT 
            area_name,
            count(*) as suitable_count
        FROM
            vacancy
            JOIN area ON vacancy.area_id = area.area_id
        WHERE
            work_schedule = 'Удаленная работа'
            AND disabled = FALSE
            AND archived = FALSE
            AND YEAR(creation_time) BETWEEN 2021 AND 2022
        GROUP BY
            area_name
    ) as suitable_vacancies
    RIGHT JOIN 
    (
        SELECT 
            area_name,
            count(*) as total_count
        FROM
            vacancy
            JOIN area ON vacancy.area_id = area.area_id
        WHERE
            disabled = FALSE
            AND archived = FALSE
            AND YEAR(creation_time) BETWEEN 2021 AND 2022
        GROUP BY
            area_name
    ) as total_vacancies
    ON suitable_vacancies.area_name = total_vacancies.area_name
ORDER BY 
    proportion_suitable_vacancies DESC;
