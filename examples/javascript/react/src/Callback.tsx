import { useFiefAuth } from '@fief/fief/react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Callback: React.FunctionComponent = () => {
  const fiefAuth = useFiefAuth();  // (1)!
  const navigate = useNavigate();

  useEffect(() => {
    fiefAuth.authCallback(`${window.location.protocol}//${window.location.host}/callback`).then(() => {  // (2)!
      navigate('/');
    });
  }, [fiefAuth, navigate]);

  return (
    <p>Callback!</p>
  );
};

export default Callback;
