const fief = require('@fief/fief');
const fiefExpress = require('@fief/fief/express');
const express = require('express');

const PORT = 3000;

const fiefClient = new fief.Fief({  // (1)!
  baseURL: 'https://fief.mydomain.com',
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET',
});

const fiefAuthMiddleware = fiefExpress.createMiddleware({  // (2)!
  client: fiefClient,  // (3)!
  tokenGetter: fiefExpress.authorizationSchemeGetter(),  // (4)!
});

const app = express();

app.get('/authenticated', fiefAuthMiddleware(), (req, res) => {  // (5)!
  res.json(req.accessTokenInfo);  // (6)!
});

app.get('/authenticated-scope', fiefAuthMiddleware({ scope: ['openid', 'required_scope'] }), (req, res) => {  // (7)!
  res.json(req.accessTokenInfo);
});

app.get('/authenticated-permissions', fiefAuthMiddleware({ permissions: ['castles:read'] }), (req, res) => {  // (8)!
  res.json(req.accessTokenInfo);
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`)
});
