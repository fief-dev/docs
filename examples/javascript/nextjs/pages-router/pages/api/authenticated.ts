import { fiefAuth } from '../../fief';

export default fiefAuth.authenticated(function handler(req, res) {
  res.status(200).json(req.user);
});
