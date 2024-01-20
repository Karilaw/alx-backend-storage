-- Write a SQL script that lists all bands with Glam rock
SELECT band_name, (2022 - formed - IFNULL(split, 0)) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
