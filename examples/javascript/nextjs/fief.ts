import { Fief, FiefUserInfo } from '@fief/fief';
import { FiefAuth, IUserInfoCache } from '@fief/fief/nextjs';

export const SESSION_COOKIE_NAME = "user_session";  // (1)!

export const fiefClient = new Fief({  // (2)!
  baseURL: 'https://example.fief.dev',
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET',
});

class MemoryUserInfoCache implements IUserInfoCache {  // (3)!
  private storage: Record<string, any>;

  constructor() {
    this.storage = {};
  }

  async get(id: string): Promise<FiefUserInfo | null> {
    const userinfo = this.storage[id];
    if (userinfo) {
      return userinfo;
    }
    return null;
  }

  async set(id: string, userinfo: FiefUserInfo): Promise<void> {
    this.storage[id] = userinfo;
  }

  async remove(id: string): Promise<void> {
    this.storage[id] = undefined;
  }

  async clear(): Promise<void> {
    this.storage = {};
  }
}

export const fiefAuth = new FiefAuth({  // (4)!
  client: fiefClient,  // (5)!
  sessionCookieName: SESSION_COOKIE_NAME,  // (6)!
  redirectURI: 'http://localhost:3000/auth-callback',  // (7)!
  logoutRedirectURI: 'http://localhost:3000',  // (8)!
  userInfoCache: new MemoryUserInfoCache(),  // (9)!
});
