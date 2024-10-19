import type { NextRequest } from 'next/server';

import { fiefAuth } from './fief';  // (1)!

const authMiddleware = fiefAuth.middleware([  // (2)!
  {
    matcher: '/private',  // (3)!
    parameters: {},
  },
  {
    matcher: '/castles/:path*',  // (4)!
    parameters: {
      permissions: ['castles:read'],  // (5)!
    },
  },
]);

export async function middleware(request: NextRequest) {  // (6)!
  return authMiddleware(request);  // (7)!
};
