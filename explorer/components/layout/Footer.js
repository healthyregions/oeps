import styles from "./Footer.module.css";

export default function Footer({ position, bottom }) {
  return (
    <footer className={styles.footer} style={{ position, bottom }}>
      <a
        href="https://www.healthyregions.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        {/* <span className={styles.logo}> */}
          <img src="/herop_light_logo.png" height={30}/>
        {/* </span> */}

      </a>
    </footer>
  );
}
