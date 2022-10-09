import { useFiefAuth, useFiefIsAuthenticated } from '@fief/fief/react';
import React, { useEffect } from 'react';

const RequireAuth: React.FunctionComponent<React.PropsWithChildren> = ({ children }) => {
  const fiefAuth = useFiefAuth();  // (1)!
  const isAuthenticated = useFiefIsAuthenticated(); // (2)!

  useEffect(() => {
    if (!isAuthenticated) {
      fiefAuth.redirectToLogin(`${window.location.protocol}//${window.location.host}/callback`);  // (3)!
    }
  }, [fiefAuth, isAuthenticated]);

  return (
    <>
      {isAuthenticated && children}
    </>
  );
};

export default RequireAuth;
