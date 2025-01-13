import '../styles/globals.scss';
import {ComponentClass, useState, Suspense, createContext} from 'react';
import {Hydrate, QueryClient, QueryClientProvider} from 'react-query';
import _ from 'lodash';
import {AnimatePresence} from 'framer-motion';
import {createTheme, ThemeProvider} from '@mui/material';
import {Toaster} from 'react-hot-toast';

interface MyappProps {
  Component: ComponentClass;
  pageProps: object;
}

const THEME = createTheme({
  typography: {
    fontFamily: `"Roboto", "Helvetica", "Arial", sans-serif`,
    fontSize: 18,
    fontWeightLight: 300,
    fontWeightRegular: 400,
    fontWeightMedium: 500,
  },
});

export const UserSessionContext = createContext<{
  token: string | null;
  onLogout: () => void;
} | null>(null);

function MyApp({Component, pageProps}: MyappProps) {
  const [queryClient] = useState(() => new QueryClient());

  return (
    <div>
        <ThemeProvider theme={THEME}>
          <QueryClientProvider client={queryClient}>
            <Hydrate state={_.get(pageProps, 'dehydratedState')}>
              <Suspense fallback={<div>Loading...</div>}>
                <Toaster />
                <AnimatePresence exitBeforeEnter onExitComplete={() => window.scrollTo(0, 0)}>
                  <Component {...pageProps} />
                </AnimatePresence>
              </Suspense>
            </Hydrate>
          </QueryClientProvider>
        </ThemeProvider>
    </div>
  );
}

export default MyApp;
