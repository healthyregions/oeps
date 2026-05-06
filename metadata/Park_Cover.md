**Meta Data Name**: Parks and Green Space Coverage
**Date Added**: May 30, 2022
**Author**: Christian Villanueva
**Date Last Modified**: January 3, 2024
**Last Modified By**: Wataru Morioka

### Data Source(s) Description:
Land use data were pulled from [OpenStreetMap (OSM)](openstreetmap.org). The following queries were made at the national level:
* natural=wood
* leisure=nature_reserve
* landuse=recreation_ground
* landuse=grass
* landuse=forest
* landuse=cemetery
* leisure=garden

### Description of Data Processing: 
Data was collected from OpenStreetMap. The queries resulted in a series of polygons representing parks and green spaces. These polygons were dissolved and unioned. The resulting geometries were broken down by county or state to result in the total area of parks and green spaces as well as the percent cover.

### Data Limitations:

Due to differences in geometry between OSM and census tigerlines, there are 2 counties with over 100% parks cover, both of which

### Comments/Notes:

NA
