SELECT 
    tabTable.*, geoTable.geom 
FROM 
    PROJECT_ID.spatial.counties2018 geoTable INNER JOIN PROJECT_ID.tabular.C_Latest tabTable
ON
    tabTable.HEROP_ID = geoTable.HEROP_ID
