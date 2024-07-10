import variables from './config/variables.json';
import data from './config/map-config-data.json';

const defaultVariable = "Opioid Mortality Rate";
const defaultData = "US Counties";

// 2 is zcta, 3 is tracts
data[2]['tiles'] = process.env.NEXT_PUBLIC_MAPBOX_TILESET_ID_ZCTA
data[3]['tiles'] = process.env.NEXT_PUBLIC_MAPBOX_TILESET_ID_TRACT

let style = {
  variableHeaders: {},
  tooltip: {
    displayOnlyCurrentVariable: true
  },
  // this layer must be present in the style defined below
  underLayerId: 'water',
  mapboxStyle: process.env.NEXT_PUBLIC_MAPBOX_STYLE
}

export const dataPresets = {
  data,
  variables,
  style,
  defaultVariable,
  defaultData
};