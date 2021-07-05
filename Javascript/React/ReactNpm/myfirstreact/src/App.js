import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet'
import Welcome from './components/Welcome'
import Hello from './components/Hello';
import Follow from './components/Follow';
import FunctionClick from './components/FunctionClick';
import Classclick from './components/Classclick';
import EventBind from './components/EventBind';
import ParentComponent from './components/ParentComponent';
import Usergreeting from './components/Usergreeting';
import Namelist from './components/Namelist';

function App() {
  return (
    <div className="App">
      {/* <Greet name="Giegie" nickName="Giao"> <p>DNLM</p><p>DNLM</p><p>DNLM</p></Greet>
      <Greet name="BBTang" nickName="Aoligei" ><button>btn1</button></Greet>
      <Greet name="NPyou" nickName="Laoba" ><button>btn2</button></Greet>
      <Welcome name="Giegie" nickName="Giao" />
      <Welcome name="BBTang" nickName="Aoligei" />
      <Welcome name="NPyou" nickName="Laoba" />
      <Hello />
      <Follow />
      <FunctionClick />
      <Classclick />
      <EventBind />
       */}


      <Namelist />

      {/* <StateCounter /> */}


      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          hello dlorw
        </p>
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
