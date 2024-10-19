import { useFiefIsAuthenticated, useFiefUserinfo } from '@fief/fief/nextjs/react';
import Link from 'next/link';
import React from 'react';

const Header: React.FunctionComponent = () => {
  const isAuthenticated = useFiefIsAuthenticated(); /* (1)! */
  const userinfo = useFiefUserinfo();

  return (
    <ul>
      <li><Link href="/">Public page</Link></li>
      <li><Link href="/private">Private page</Link></li>
      <li>
        Castles
        <ul>
          <li><Link href="/castles">Index</Link></li>
          <li><Link href="/castles/create">Create</Link></li>
        </ul>
      </li>
      <li>
        {/* (2)! */}
        {!isAuthenticated && <Link href="/login">Login</Link>}
        {isAuthenticated && userinfo && (
          <div>
            <span>{userinfo.email} - </span>
            {/* (3)! */}
            <Link href="/logout">Logout</Link>
          </div>
        )}
      </li>
    </ul>
  );
};

export default Header;
