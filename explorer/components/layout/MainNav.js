import Link from 'next/link';
import "@reach/menu-button/styles.css";
import styles from "./MainNav.module.css";
import {useRouter} from "next/router";

import {
  Menubar,
  MenuRoot,
  MenuTrigger,
  MenuPortal,
  MenuPositioner,
  MenuPopup,
  MenuItem
} from './Menubar';

export default function MainNav() {
  const router = useRouter();

  return (
    <div className={styles.masthead} style={{ display: 'flex', justifyContent: 'space-between'}}>
      <h3 className={styles.mastheadTitle} color='black'>
        <Link href="/">OEPS Ecosystem</Link>
      </h3>
      <nav className={styles.mainNav}>
        <Menubar>

          <MenuRoot>
            <MenuTrigger onClick={() => router.push('/')}>Home</MenuTrigger>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>About</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/about')}>About OEPS</MenuItem>
                   <MenuItem onClick={() => router.push('/posts')}>News & Updates</MenuItem>
                   <MenuItem onClick={() => router.push('/methods')}>Methodology</MenuItem>
                   <MenuItem onClick={() => router.push('/dataInclusion')}>Data Inclusion Criteria</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Explore</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/docs')}>Data Inventory</MenuItem>
                  <MenuItem onClick={() => router.push('/map')}>Map Explorer</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Data Access</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/download')}>Download</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Resources</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/codeResources')}>Code & Analytic Resources</MenuItem>
                  <MenuItem onClick={() => router.push('/insights')}>Research Insights</MenuItem>
                  <MenuItem onClick={() => window.open('https://gccp.healthyregions.org', '_blank')}>GCCP Community</MenuItem>
                  <MenuItem onClick={() => window.open('https://www.jcoinctc.org/tta/', '_blank')}>TA Support</MenuItem>
                  <MenuItem onClick={() => window.open('https://healthyregions.github.io/oeps/', '_blank')}>For Developers<br/>(OEPS Data Ecosystem)</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger onClick={() => router.push('/contact')}>Contact</MenuTrigger>
          </MenuRoot>
        </Menubar>
      </nav>
    </div>
  );
}
