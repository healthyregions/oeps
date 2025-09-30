import Head from "next/head";
import styles from "../styles/Map.module.css";

import MainNav from "../components/layout/MainNav";
import MainMap from "../components/map/MainMap";
import VariablePanel from "../components/map/VariablePanel";
import MapTooltip from "../components/map/MapTooltip";

// import useLoadData from '@webgeoda/hooks/useLoadData'
// import useUpdateData from '@webgeoda/hooks/useUpdateData'
import rootReducer from "../_webgeoda/reducers";
import {GeodaContext, ViewportProvider} from "../_webgeoda/contexts";

import { createStore } from "redux";
import { Provider } from "react-redux";
import { useEffect, useState } from "react";
import * as Comlink from "comlink";
import { Grommet } from 'grommet';

const oepsTheme = {
  global: {
    font: {
      family: '"Lato", Verdana, Geneva, Tahoma, sans-serif'
    },
    colors: {
      brand: '#449D8F'
    }
  },
};

const store = createStore(
  rootReducer,
  // (
  //   typeof window === 'object'
  //   && window.__REDUX_DEVTOOLS_EXTENSION__
  //   && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
  // ) && window.__REDUX_DEVTOOLS_EXTENSION__({
  //   stateSanitizer: (state) => state.storedGeojson ? { ...state, storedData: '<<EXCLUDED>>', storedGeojson: '<<EXCLUDED>>' } : state
  // })
);

var geoda;

export default function Map() {
  const [geodaReady, setGeodaReady] = useState(false);

  useEffect(() => {
    geoda = Comlink.wrap(new Worker("./workers/worker.jsgeoda.js"));
    geoda
      .New()
      .then(() => setGeodaReady(true))
      .then(() => geoda.listFunctions());
  }, []);

  return (
    <div className={styles.container}>
      <Head>
        <title>Map :: OEPS </title>
        <link
          href="https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.css"
          rel="stylesheet"
        />
      </Head>
      <MainNav />
      {/* {!geodaReady && <div className={styles.preLoader}><Loader globe={true} /></div>} */}

        <ViewportProvider>
          <Provider store={store}>
            {geodaReady && (
              <GeodaContext.Provider value={geoda}>
                <Grommet theme={oepsTheme}>
                  <MainMap geoda={geoda} />
                  <VariablePanel />
                  <MapTooltip />
                </Grommet>
              </GeodaContext.Provider>
            )}
          </Provider>
        </ViewportProvider>
    </div>
  );
}
