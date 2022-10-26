import { useFiefAccessTokenInfo } from '@fief/fief/nextjs';
import type { NextPage } from 'next';

const CastlesCreate: NextPage = () => {
  const accessTokenInfo = useFiefAccessTokenInfo();

  return (
    <>
      <h2>You have the following permissions:</h2>
      <ul>
        {accessTokenInfo?.permissions.map((permission) => <li key={permission}>{permission}</li>)}
      </ul>
    </>
  );
};

export default CastlesCreate;
