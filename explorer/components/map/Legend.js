import styles from "./MainMap.module.css";
import { formatLegendLabel } from "../../_webgeoda/utils/formatMapNumeric";

export default function Legend(props) {
  return (
    <div className={styles.legendContainer}>
      {props.variableName && (
        <p className={styles.variableName}>{props.variableName}</p>
      )}
      <div className={styles.legendInnerContainer}>
        <div className={`${styles.legendColors} ${props.ordinal && styles.categoricalLegendColors}`}>
          {props.colors?.map((color, i) => (
            <span
              key={`legend-color-${i}`}
              style={{ backgroundColor: `rgb(${color.join(",")})` }}
            ></span>
          ))}
        </div>
        <div className={`${styles.legendLabels} ${props.ordinal && styles.categoricalLegendLabels}`}>
          {props.bins?.map((bin, i) => (
            <span key={`legend-label-${i}`}>{formatLegendLabel(bin)}</span>
          ))}
        </div>
      </div>
    </div>
  );
}
