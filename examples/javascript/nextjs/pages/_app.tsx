import { FiefAuthProvider } from '@fief/fief/nextjs/react';
import type { AppProps } from 'next/app';

import Header from '../components/Header/Header';

import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <FiefAuthProvider currentUserPath="/api/current-user"> {/* (1)! */}
      <Header /> {/* (2)! */}
      <Component {...pageProps} />
    </FiefAuthProvider>
  );
};

export default MyApp;
