CREATE TABLE vacancy (
  vacancy_id INT,
  name STRING,
  work_schedule STRING,
  disabled BOOLEAN,
  area_id INT,
  creation_time STRING,
  archived BOOLEAN
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE resume (
  resume_id INT,
  disabled BOOLEAN,
  is_finished INT,
  area_id INT,
  compensation BIGINT,
  currency STRING,
  position STRING,
  birth_day TIMESTAMP,
  role_id_list ARRAY<INT>
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE area (
  area_id INT,
  area_name STRING,
  region_name STRING,
  country_name STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE currency (
  code STRING,
  rate DECIMAL(10, 2)
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
