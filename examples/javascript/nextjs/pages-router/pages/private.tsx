import { useFiefUserinfo } from '@fief/fief/nextjs/react';
import type { NextPage } from 'next';

const Private: NextPage = () => {
  const user = useFiefUserinfo(); // (1)!

  return (
    <h2>You are authenticated. Your user email is {user?.email}</h2>
  )
};

export default Private;
