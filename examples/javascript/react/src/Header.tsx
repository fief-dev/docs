import { useFiefAuth, useFiefIsAuthenticated, useFiefUserinfo } from '@fief/fief/react';
import React, { useCallback } from 'react';
import { Link } from 'react-router-dom';

const Header: React.FunctionComponent = () => {
  const fiefAuth = useFiefAuth();
  const isAuthenticated = useFiefIsAuthenticated();
  const userinfo = useFiefUserinfo();  // (1)!

  const login = useCallback(() => {  // (2)!
    fiefAuth.redirectToLogin(`${window.location.protocol}//${window.location.host}/callback`);
  }, [fiefAuth]);

  const logout = useCallback(() => {  // (3)!
    fiefAuth.logout(`${window.location.protocol}//${window.location.host}`);
  }, [fiefAuth]);

  return (
    <ul>
      <li><Link to="/">Public page</Link></li>
      <li><Link to="/private">Private page</Link></li>
      <li>
        {!isAuthenticated && <button type="button" onClick={() => login()}>Login</button>}
        {isAuthenticated && userinfo && (
          <div>
            <span>{userinfo.email}</span>
            <button type="button" onClick={() => logout()}>Logout</button>
          </div>
        )}
      </li>
    </ul>
  );
};

export default Header;
