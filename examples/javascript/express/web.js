const fief = require('@fief/fief');
const fiefExpress = require('@fief/fief/express');
const express = require('express');

const SESSION_COOKIE_NAME = "user_session"  // (1)!
const PORT = 3000;
const REDIRECT_URI = `http://localhost:${PORT}/auth-callback`;  // (2)!

class MemoryUserInfoCache {  // (3)!
  constructor() {
    this.storage = {};
  }

  async get(id) {
    const userinfo = this.storage[id];
    if (userinfo) {
      return userinfo;
    }
    return null;
  }

  async set(id, userinfo) {
    this.storage[id] = userinfo;
  }

  async remove() {
    this.storage[id] = undefined;
  }

  async clear() {
    this.storage = {};
  }
}

const userInfoCache = new MemoryUserInfoCache();

const fiefClient = new fief.Fief({  // (4)!
  baseURL: 'https://example.fief.dev',
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET',
});

const unauthorizedResponse = async (req, res) => {  // (5)!
  const authURL = await fiefClient.getAuthURL({ redirectURI: REDIRECT_URI, scope: ['openid'] });  // (6)!
  res.redirect(307, authURL);  // (7)!
};

const fiefAuthMiddleware = fiefExpress.createMiddleware({
  client: fiefClient,
  tokenGetter: fiefExpress.cookieGetter(SESSION_COOKIE_NAME),  // (8)!
  unauthorizedResponse,  // (9)!
  userInfoCache,  // (10)!
});

const app = express();

app.get('/auth-callback', async (req, res) => {  // (11)!
  const code = req.query['code'];
  const [tokens, userinfo] = await fiefClient.authCallback(code, REDIRECT_URI);  // (12)!

  userInfoCache.set(userinfo.sub, userinfo);  // (13)!

  res.cookie(  // (14)!
    SESSION_COOKIE_NAME,
    tokens.access_token,
    {
      maxAge: tokens.expires_in * 1000,
      httpOnly: true,  // (15)!
      secure: false,  // ❌ Set this to `true` in production (16)!
    },
  );
  res.redirect('/protected');
});

app.get('/protected', fiefAuthMiddleware(), (req, res) => {  // (17)!
  res.send(`<h1>You are authenticated. Your user email is ${req.user.email}</h1>`)  // (18)!
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`)
});
