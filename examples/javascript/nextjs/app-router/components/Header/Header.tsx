import { FiefUserInfo } from '@fief/fief';
import Link from 'next/link';
import React from 'react';

interface HeaderProps {
  userinfo: FiefUserInfo | null
}

const Header: React.FunctionComponent<HeaderProps> = ({ userinfo }) => {

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
        {!userinfo && <Link href="/login">Login</Link>}
        {userinfo && (
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
