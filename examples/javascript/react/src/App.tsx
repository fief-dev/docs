import { FiefAuthProvider } from '@fief/fief/react';
import { Routes, Route } from 'react-router-dom';

import Callback from './Callback';
import Public from './Public';
import Private from './Private';
import Header from './Header';
import RequireAuth from './RequireAuth';

function App() {
  return (
    <FiefAuthProvider // (1)!
      baseURL="https://fief.mydomain.com"
      clientId="NFL8Ycdag-gbvO-5pJezwCmFEouCDRhCG4paUNOaDoI"
    >
      <div className="App">
        <h1>Fief React example</h1>
        <Header />  {/* (2)! */}
        <Routes>  {/* (3)! */}
          <Route path="/" element={<Public />} /> {/* (4)! */}
          <Route path="/private" element={<RequireAuth><Private /></RequireAuth>} /> {/* (5)! */}
          <Route path="/callback" element={<Callback />} /> {/* (6)! */}
        </Routes>
      </div>
    </FiefAuthProvider>
  );
}

export default App;
