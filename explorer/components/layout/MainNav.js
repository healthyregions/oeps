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
  MenuItem,
} from './Menubar';

export default function MainNav() {
  const router = useRouter();

  return (
    <div className={styles.masthead} style={{ display: 'flex', justifyContent: 'space-between'}}>
      <h3 className={styles.mastheadTitle} color='black'>
        <Link href="/">OEPS Ecosystem</Link>
      </h3>
      <nav>
        <Menubar>

          <MenuRoot>
            <MenuTrigger onClick={() => router.push('/')}>Home</MenuTrigger>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>About</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/about')}>Teams</MenuItem>
                  <MenuItem onClick={() => router.push('/insights')}>Insights</MenuItem>
                  <MenuItem onClick={() => router.push('/posts')}>News</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Explore</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/map')}>Map</MenuItem>
                  <MenuItem onClick={() => router.push('/download')}>Data</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Documentation</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/docs')}>Metadata</MenuItem>
                  <MenuItem onClick={() => router.push('/methods')}>Methods</MenuItem>
                  {/*<MenuSubmenuRoot>*/}
                  {/*  <MenuSubmenuTrigger>Methodology</MenuSubmenuTrigger>*/}
                  {/*  <MenuPortal>*/}
                  {/*    <MenuPositioner alignOffset={-4}>*/}
                  {/*      <MenuPopup>*/}
                  {/*        <MenuItem onClick={() => router.push('/methods')}>Methods</MenuItem>*/}
                  {/*        <MenuItem onClick={() => router.push('/dataInclusion')}>Data Inclusion</MenuItem>*/}
                  {/*      </MenuPopup>*/}
                  {/*    </MenuPositioner>*/}
                  {/*  </MenuPortal>*/}
                  {/*</MenuSubmenuRoot>*/}
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          <MenuRoot>
            <MenuTrigger>Resources</MenuTrigger>
            <MenuPortal>
              <MenuPositioner alignOffset={-4}>
                <MenuPopup>
                  <MenuItem onClick={() => router.push('/codeResources')}>Notebooks</MenuItem>
                  {/*<MenuItem onClick={() => router.push('/workshops')}>Workshops</MenuItem>*/}
                  <MenuItem onClick={() => window.open('https://healthyregions.github.io/oeps/', '_blank')}>For Developers<br/>(OEPS Data Ecosystem)</MenuItem>
                </MenuPopup>
              </MenuPositioner>
            </MenuPortal>
          </MenuRoot>

          {/*<MenuRoot>*/}
          {/*  <MenuTrigger onClick={() => router.push('/contact')}>Contact</MenuTrigger>*/}
          {/*</MenuRoot>*/}
        </Menubar>
      </nav>
    </div>
  );
}
