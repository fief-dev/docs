import { Fief, FiefUserInfo } from '@fief/fief';
import { FiefAuth, IUserInfoCache } from '@fief/fief/nextjs';

export const SESSION_COOKIE_NAME = "user_session";  // (1)!

export const fiefClient = new Fief({  // (2)!
  baseURL: 'http://localhost:8000',
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET',
  requestInit: { next: { revalidate: 3600 } },
});

export const fiefAuth = new FiefAuth({  // (3)!
  client: fiefClient,  // (4)!
  sessionCookieName: SESSION_COOKIE_NAME,  // (5)!
  redirectURI: 'http://localhost:3000/auth-callback',  // (6)!
  logoutRedirectURI: 'http://localhost:3000',  // (7)!
});
