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
import StyleSheet from './components/StyleSheet';
import Inline from './components/Inline';
import Form from './components/Form';
import Form2 from './components/Form2';
import Lc from './components/Lc';
import FragmentReact from './components/FragmentReact';
import Table from './components/Table';
import ParentComp from './components/ParentComp';
import RefsDemo from './components/RefsDemo';
import FocusInput from './components/FocusInput';
import RFParentInput from './components/RFParentInput';
import NonStringRef from './components/NonStringRef';
import FuncRef from './components/FuncRef';
import RefCreateRef from './components/RefCreateRef';
import ReactEventHandle from './components/ReactEventHandle';
import NonControlledComponent from './components/NonControlledComponent';
import ControlledComponent from './components/ControlledComponent';
import Curring from './components/Curring';
import ReactLifeCycle from './components/ReactLifeCycle';
import Lifecycle2 from './components/Lifecycle2';


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

      <StyleSheet primary={true} />
      <Lifecycle2 />

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
