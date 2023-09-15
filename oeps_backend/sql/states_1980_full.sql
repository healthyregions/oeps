SELECT 
    tabTable.*, geoTable.geom 
FROM 
    PROJECT_ID.spatial.states2010 geoTable INNER JOIN PROJECT_ID.tabular.S_1980 tabTable
ON
    tabTable.HEROP_ID = geoTable.HEROP_ID
