import { FiefAuthProvider } from '@fief/fief/nextjs/react';
import type { AppContext, AppProps, AppInitialProps } from 'next/app';
import App from 'next/app';

import Header from '../components/Header/Header';

import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <FiefAuthProvider state={{ accessTokenInfo: null, userinfo: null }} currentUserPath="/api/current-user"> {/* (1)! */}
      <Header /> {/* (2)! */}
      <Component {...pageProps} />
    </FiefAuthProvider>
  );
};

MyApp.getInitialProps = async (
  context: AppContext
): Promise<AppInitialProps> => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx }
}

export default MyApp;
