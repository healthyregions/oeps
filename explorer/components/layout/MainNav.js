import Link from 'next/link';
import {Menu, MenuButton, MenuLink} from "@reach/menu-button";
import "@reach/menu-button/styles.css";
import styles from "./MainNav.module.css";
import {NestedDropdown} from "mui-nested-menu";
import {useRouter} from "next/router";
import {MenuList} from "@mui/material";
import {MenuItemData} from "mui-nested-menu";

import {
  Menubar,
  MenuRoot,
  MenuTrigger,
  MenuPortal,
  MenuPositioner,
  MenuPopup,
  MenuItem,
  MenuSeparator,
  MenuSubmenuRoot,
  MenuSubmenuTrigger,
} from './Menubar';

export default function MainNav() {
  const router = useRouter();

  const menuItemsData = {
    label: 'Menu',
    rightIcon: <>☰</>,
    items: [
      {
        label: 'Home',
        callback: (event, item) => router.push('/'),
      },
      {
        label: 'About',
        items: [
          {
            label: 'Teams',
            callback: (event, item) => router.push('/about'),
          },
          {
            label: 'Insights',
            callback: (event, item) => router.push('/insights'),
          },
          {
            label: 'Posts',
            callback: (event, item) => router.push('/posts'),
          }
        ]
      },
      {
        label: 'Explore',
        items: [
          {
            label: 'Map',
            callback: (event, item) => router.push('/map'),
          },
          {
            label: 'Data',
            callback: (event, item) => router.push('/download'),
          },
        ]
      },
      {
        label: 'Documentation',
        items: [
          {
            label: 'Metadata',
            callback: (event, item) => router.push('/docs'),
          },
          {

            label: 'Methodology',
            items: [
              {
                label: 'Methods',
                callback: (event, item) => router.push('/methods'),
              },
              // TODO: for "Data Inclusion" new page
              // {
              //   label: 'Data Inclusion',
              //   callback: (event, item) => router.push('/dataInclusion'),
              // },
            ]
          }
        ]
      },
      {
        label: 'Resources',
        //leftIcon: <SaveIcon />,
        items: [
          {
            label: 'Notebooks',
            callback: (event, item) => router.push('/codeResources'),
          },
          {
            label: 'Workshops',
            callback: (event, item) => router.push('/insights'),
          },
          {
            label: 'For Developers (OEPS Data Ecosystem)',
            callback: (event, item) => window.open('https://healthyregions.github.io/oeps/', '_blank'),
          }]
      },
      {
        label: 'Contact',
        //leftIcon: <SaveIcon />,
        callback: (event, item) => router.push('/contact'),
      },
    ],
  };


  return (
    <div className={styles.masthead} style={{ display: 'flex', justifyContent: 'space-between'}}>
      <h3 className={styles.mastheadTitle} color='black'>
        <Link href="/">OEPS Ecosystem</Link>
      </h3>
      <nav>
          {/*<NestedDropdown*/}
          {/*  menuItemsData={menuItemsData}*/}
          {/*  MenuProps={{ elevation: 3, dir: 'rtl' }}*/}
          {/*  ButtonProps={{*/}
          {/*    color: 'inherit',*/}
          {/*    sx: {*/}
          {/*      fontSize: '13px',*/}
          {/*      margin: 0,*/}
          {/*      textTransform: 'none'*/}
          {/*    },*/}
          {/*    endIcon: <>☰</>*/}
          {/*  }}>*/}
          {/*</NestedDropdown>*/}
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
