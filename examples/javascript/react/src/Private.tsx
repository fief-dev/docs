import { useFiefUserinfo } from '@fief/fief/react';

const Private: React.FunctionComponent = () => {
  const userinfo = useFiefUserinfo();

  return (
    <>
      <h2>This is a private page for {userinfo?.email}</h2>
    </>
  );
};

export default Private;
