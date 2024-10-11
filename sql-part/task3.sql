CREATE TABLE age_ranges(
    start_age INT,
    end_age INT,
    age_group STRING
);

INSERT INTO age_ranges VALUES (0, 17, '17 лет и младше');
INSERT INTO age_ranges VALUES (18, 24, '18–24');
INSERT INTO age_ranges VALUES (25, 34, '25–34');
INSERT INTO age_ranges VALUES (35, 44, '35–44');
INSERT INTO age_ranges VALUES (45, 54, '45–54');
INSERT INTO age_ranges VALUES (55, 200, '55 и старше');


SELECT
    sub_table.area_name as city,
    age_ranges.age_group as age_group,
    COUNT(sub_table.salary) * 1.0 / COUNT(*) AS salary_share,
    PERCENTILE_DISC(sub_table.salary, 0.1) AS percentile_10,
    PERCENTILE_DISC(sub_table.salary, 0.25) AS percentile_25,
    PERCENTILE_DISC(sub_table.salary, 0.5) AS percentile_50,
    PERCENTILE_DISC(sub_table.salary, 0.75) AS percentile_75,
    PERCENTILE_DISC(sub_table.salary, 0.9) AS percentile_90
FROM 
    (
        SELECT 
            area_name,
            FLOOR(DATEDIFF(CURRENT_DATE, birth_day) / 365) AS age,
            compensation * rate AS salary
        FROM 
            resume
            LEFT JOIN area ON resume.area_id = area.area_id
            LEFT JOIN currency ON resume.currency = currency.code
        WHERE
            area_name IN ('Москва', 'Санкт-Петербург')
            AND array_contains(role_id_list, 91)
            AND birth_day IS NOT NULL
            AND disabled = FALSE
            AND is_finished = 1
    ) as sub_table
    JOIN age_ranges ON sub_table.age BETWEEN age_ranges.start_age AND age_ranges.end_age
GROUP BY
    sub_table.area_name, age_ranges.age_group;


DROP TABLE age_ranges;
