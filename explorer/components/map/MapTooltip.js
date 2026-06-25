import { useState, useEffect } from 'react';
import styles from "./MainMap.module.css";
import { useSelector } from "react-redux";
import { handleLoadData } from '../../_webgeoda/utils/data'
import { formatMapNumeric } from '../../_webgeoda/utils/formatMapNumeric'

const formatTooltipValue = (value) => {
  if (value === null || value === undefined || value === '') return value
  const n = Number(value)
  return Number.isFinite(n) ? formatMapNumeric(n) : String(value)
}

const pad = (val, len, padChar) => `${val}`.length >= len ? ''+val : pad(`${padChar}${val}`, len, padChar)

/** GEOID suffix from HEROP_ID (e.g. 860US61801 → 61801); passthrough for legacy numeric ids. */
const geoidFromId = (id) => {
  if (id === null || id === undefined || id === '') return null
  const s = String(id)
  if (/^\d{3}US/.test(s) && s.length > 5) return s.slice(5)
  return s
}

const findTractStateAndCounty = ({countyDict, id}) => {
  const idVal = pad(geoidFromId(id), 11, 0)
  const county = countyDict[+idVal.slice(0, 5)]
  return county?.Name + ' County, ' + county?.State
}

const TooltipTitle = ({currentData, stateDict, countyDict, id}) => {
  if (!currentData) return null
  const geoid = geoidFromId(id)
  const text = currentData.includes('state')
    ? stateDict[geoid]?.State ?? stateDict[+geoid]?.State ?? stateDict[id]?.State
    : currentData.includes('count')
    ? (countyDict[geoid]?.Name ?? countyDict[+geoid]?.Name ?? countyDict[id]?.Name) +
      ', ' +
      (countyDict[geoid]?.State ?? countyDict[+geoid]?.State ?? countyDict[id]?.State)
    : currentData.includes('Zip')
    ? 'Zip Code: ' + pad(geoid, 5, 0)
    : findTractStateAndCounty({countyDict, id})

  if (text === undefined || (typeof text === 'string' && text.includes('undefined'))) return null
  return <span>
    <h2 className="tooltip-header">{text}</h2>
    {currentData.includes('Tract') && <h4>Tract# {pad(geoid, 11, 0)}</h4>}
    </span>
}

export default function MapTooltip() {
  const [stateDict, setStateDict] = useState({});
  const [countyDict, setCountyDict] = useState({});
  const currentHoverTarget = useSelector((state) => state.currentHoverTarget);
  const currentData = useSelector((state) => state.currentData);

  useEffect(() => {
    Promise.all([
      handleLoadData({
        file:'counties.csv',
        join:'FIPS'
      }),
      handleLoadData({
        file:'states.csv',
        join:'FIPS'
      })
    ]).then(([counties,states]) => {
      setCountyDict(counties.data)
      setStateDict(states.data)
    })
  },[])

  if (!(typeof window) || !currentHoverTarget.data) return null;

  const rightSide = currentHoverTarget.x > window.innerWidth / 2
  const bottomSide = currentHoverTarget.y > window.innerHeight / 2
  const [ 
    xProp, 
    x,
    yProp,
    y
  ] = [
    rightSide ? 'right' : 'left',
    rightSide ? window.innerWidth - currentHoverTarget.x : currentHoverTarget.x,
    bottomSide ? 'bottom' : 'top',
    bottomSide ? window.innerHeight - currentHoverTarget.y - 50: currentHoverTarget.y + 50,
  ]
  
  return (
    <div
      className={styles.tooltipContainer}
      style={{ [xProp]: x, [yProp]: y, display: x === null ? 'none' : 'block' }}
    >
      <TooltipTitle   
        currentData={currentData}
        stateDict={stateDict}
        countyDict={countyDict}
        id={currentHoverTarget.id}
      />
      {currentHoverTarget.data.map((entry, idx) => (
        <p key={`tooltip-${entry.value}-${idx}`}>

          <b>{entry.name}</b>: {formatTooltipValue(entry.value)}
        </p>
      ))}
    </div>
  );
}
