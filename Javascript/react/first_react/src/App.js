// import logo from './logo.svg';
// import './App.css';
import header from "./components/header";
import Headers from "./components/Headers";
import Thetask from "./components/Thetask";
import React from "react";
import { useState } from 'react'

function App() {
  const [task, setTasks] = useState([{
    "id": 1,
    "text": "Doctors Appointment",
    "day": "Feb 5th at 2:30pm",
    "reminder": true
  },
  {
    "id": 2,
    "text": "Meeting at School",
    "day": "Feb 6th at 1:30pm",
    "reminder": true
  },
  {
    "id": 3,
    "text": "Food Appointment",
    "day": "Feb 5th at 2:30pm",
    "reminder": false
  },
  ])
  return (
    // ! return must be single element
    // ! return <> ... <> is legal, but it will be wrapped in div id="root"
    <div className="container">
      <Headers />
      <Thetask tasks={task} />
    </div>

    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
  );
}


export default App;
