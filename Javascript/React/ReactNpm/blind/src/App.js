import logo from './logo.svg';
import './App.css';
import Hello from './component/Hello';
import Hello1 from './component/Hello1';
import Hellobracket from './component/Hellobracket'
import Hellowithprop from './component/Hellowithprop'
import Hellobracketwithprop from './component/Hellobracketwithprop'
import StateButton from './component/StateButton'

import StateCounter from './component/StateCounter';
import DisplayInfo from './component/DisplayInfo';



function App() {

  return (
    <div className="App">
      <Hello></Hello>
      <Hello1 />
      <Hellobracket />
      <Hellowithprop name="lily" id={2333}></Hellowithprop>
      <Hellobracketwithprop name="lily2" id={2333333}/>


      <StateButton />
      <StateCounter />
      <DisplayInfo name="alice" id="110-211" />

      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
