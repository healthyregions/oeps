import variables from './config/variables.json';

import stateData from './config/sources/state.json';
import countyData from './config/sources/county.json';
import zctaData from './config/sources/zcta.json';
import tractData from './config/sources/tract.json';

const defaultVariable = "Opioid Mortality Rate";
const defaultData = "US Counties";

const data = [
  stateData,
  countyData,
  zctaData,
  tractData
]

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