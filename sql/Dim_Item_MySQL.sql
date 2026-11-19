-- Run in MySQL Workbench, then import the table into Power BI via Get Data > MySQL database
CREATE DATABASE IF NOT EXISTS nigeria_agri;
USE nigeria_agri;
DROP TABLE IF EXISTS dim_item;
CREATE TABLE dim_item (
  Item_ID INT PRIMARY KEY,
  Item VARCHAR(200) NOT NULL,
  Crop_Category VARCHAR(60) NOT NULL,
  Is_Aggregate VARCHAR(3) NOT NULL
);
-- Load Dim_Item.csv with the Table Data Import Wizard (right-click Tables > Table Data Import Wizard)
-- or: LOAD DATA LOCAL INFILE 'C:/path/Dim_Item.csv' INTO TABLE dim_item
--     FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
SELECT Crop_Category, COUNT(*) AS items FROM dim_item GROUP BY Crop_Category;
